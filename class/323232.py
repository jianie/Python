def main():
    grades=[]
    for i in range(1,7,1):
        grade=eval(input(("Enter grade on quiz {0}: ".format(i))))
        grades.append(grade)
    g=Quizzes(grade)
    g.average(grades)
    print(g)

class Quizzes:
    def __init__(self,grade=0):
        self._grade=grade
    def setgrade(self,grade):
        self._grade=grade
    def getgrade(self):
        return self._grade
    def average(self,grades):
        grades.sort()
        del grades[0]
        self._avr=sum(grades)/5
        return self._avr
    def __str__(self):
        return ("Quiz average: "+str(self._avr))
main()



