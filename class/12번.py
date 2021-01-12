import student
def main():
    listOfStudents=ObtainListOfStudents()
    displayResults(listOfStudents)

def ObtainListOfStudents():
    listOfStudents=[]
    carryOn='Y'
    while carryOn=="Y":
        name=input("Eenter student's name: ")
        midterm=float(input("Enter student's grade on midterm exam: "))
        final=float(input("Enter student's grade on final exam: "))
        category=input("Enter category (LG or PF): ")
        if category.upper()=="LG":
            st=student.LGstudent(name,midterm,final)
        else:
            question=input("Are you a full-time student?(Y/N): ")
            if question.upper()=="Y":
                fulltime=True
            else:
                fulltime=False
            st = student.PFstudent(name, midterm, final,fulltime)
        listOfStudents.append(st)
        carryOn=input("Do you want to continue (Y/N)? ")
        carryOn=carryOn.upper()
    return listOfStudents
def displayResults(listOfStudents):
    print("\nNAME\tGRADE\tSTATUS")
    listOfStudents.sort(key=lambda x:x.getName())
    for pupil in listOfStudents:
        print(pupil)
main()
