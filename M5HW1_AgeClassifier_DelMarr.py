#CTI-110
#M5HW1 - Age Classifier
#Hasan DelMarr
#22 November 2017
#

#Defining a person's age.

Age = int(input("Enter Your Age:"))

if Age <=1:
    print ("This person is an infant.")

elif Age <=13:
    print("This person is a child.")
elif Age <=18:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
    

