#CTI-110
#M6HW3 - Factorial
#Hasan DelMarr
#2 December 2017

#Defining student integer and factorial

studentinteger = int( input( "Please Enter a Number: " ))

while studentinteger < 1:
    studentinteger = int( input( "Please Enter a non-negative Number: " ) )

factorial = 1

for number in range( 1, studentinteger + 1 ):
    factorial = factorial * number

print("The factorial of", studentinteger, "is", factorial )
