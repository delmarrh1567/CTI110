#A brief description of the project
#6 December 2017
#CTI-110 M7HW2 - Random Number Guessing Game
#Hasan DelMarr
#

number = 110
guess = -1

            
print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))
    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
