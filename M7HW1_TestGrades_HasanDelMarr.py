#A brief description of the project
#6 December 2017
#CTI-110 M7HW1 - Test Average and Grade
#Hasan DelMarr
#


def main ():
    score = input("Enter grade: ")
    grade(score)

    
def grade ( studentscore ):
    if(studentscore < 60 ):
        print ("F")
    elif(studentscore < 70 ):
        print ("D")
    elif(studentscore < 80 ) :
        print ("C")
    elif(studentscore < 90 ) :
        print ("B")
    elif (studentscore < 101 ):
        print ("A")
                
                
        

    # program start
main ()
                
