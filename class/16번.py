def main():
    principal=float(input("Enter principal amount of mortgage: "))
    interestRate=float(input("Enter percent interest rate: "))
    term=float(input("Enter duration of mortgage in years: "))
    numberOfPoints=eval(input("Enter number of discount points: "))
    mort=Mortgage(principal,interestRate,term)
    discountpoint=MortgageWithPoints(principal,interestRate,term,numberOfPoints)
    print("Cost of discount points: ${0:,.2f}".format(discountpoint.caculatePoint()))
    print("Monthly payment: ${0:,.2f}".format(mort.caculateMonthlyPayment()))

class Mortgage:
    def __init__(self,principal,interestRate,term):
        self._principal=principal
        self._interestRate=interestRate
        self._term=term
    def caculateMonthlyPayment(self):
        i=self._interestRate/1200
        return ((i/(1-(1+i)**(-12*self._term)))*self._principal)
class MortgageWithPoints(Mortgage):
    def __init__(self,principal,interestRate,term,numberOfPoints):
        super().__init__(principal,interestRate,term)
        self._numberOfPoints=numberOfPoints
    def caculatePoint(self):
        return (self._principal*self._numberOfPoints*0.01)
main()