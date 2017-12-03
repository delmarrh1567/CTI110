#CTI-110
#M6HW1 - Distance Traveled
#Hasan DelMarr
#30 November 2017

#Defining Speed and Time Traveled of Vehicle

Vehiclespeed = float( input("What is the speed of vehicle:"))
TimeTraveled = int( input("Amount of hours vehicle has traveled:"))

print("Hour", "Distance Traveled" )
for currenthour in range( 1, TimeTraveled + 1 ):
    distancetraveled = Vehiclespeed * currenthour
    print(currenthour, distancetraveled ) 
