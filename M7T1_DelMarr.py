#CTI-110
#M7T1: Kilometer Converter
#Hasan DelMarr
#4 December 2017

#Converts kilometer to miles


CONVERSION_FACTOR = 0.6212

def main():
    #Get the distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))

    show_miles(kilometers)

def show_miles (km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print (km, "kilometers equals", miles, "miles.")

main ()
