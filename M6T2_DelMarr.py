#CTI-110
#M6T2: Bug Collector
#Hasan DelMarr
#30 December 2017

#Bugs Collected for Each Day
total = 0
for day in range(1, 8):
    # Prompt the user.
    print("Enter the bugs collected on day", day)

    # Input the number of bugs.
    bugs = int(input())

    #Add bugs to total.
    total += bugs

# Display the total bugs.
print("You collected a total of", total, "bugs.")
          
