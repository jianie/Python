def main():
    grades=[]
    for i in range(1,7,1):
        grade=eval(input("Enter grade on quiz {0}: ".format(i)))
        grades.append(grade)
    g=Quizzes(grades)
    print(g)


class Quizzes:
    def __init__(self,grades=[]):
        self._grades=grades
    def setgrade(self,grades):
        self._grades=grades
    def getgrade(self):
        return self._grades
    def average(self):
        self._grades.sort()
        del self._grades[0]
        return sum(self._grades)/5
    def __str__(self):
        return ("Quiz average: {0:.2f} ".format(self.average()))
main()