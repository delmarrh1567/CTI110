# A brief description of the project
# 4 December 2017
# CTI-110 M7T2_FeetTolnches
# Hasan DelMarr

#Constant for the number of inches per foot.
INCHES_PER_FOOT = 12

# main function
def main ():
    #Get a number of feet from the user.
    feet = int(input("Enter a number of feet: "))

    #Convert that to inches.
    print(feet, "equals", feet_to_inches(feet), "inches.")
    
#Defining feet to inches

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function.
main()
