'''
WELCOME TO NUMBER GUESSING GAME


QUICK RULES:
-input any range you want
-the computer will choose a number in random in that range
-you need to guess that number
-try to guess the number in minimum number of attempt
'''
print("WELCOME TO NUMBER GUESSING GAME\n \n \n QUICK RULES:\n-input any range you want\n-the computer will choose a number in random in that range\n-you need to guess that number\n-try to guess the number in minimum number of time")

import random as r
import math as m


#User inputs the lower bound and upper bound of the range.
print("Enter the range")
lower_bound = int(input(">"))
upper_bound = int(input(">"))

#The compiler generates a random integer between the range and store it in a variable compilers_guess.

compilers_guess = r.randint(lower_bound, upper_bound)

#You can comment out below comment to check the compiler,s guess
#print(compilers_guess)



#First guess by the user
user_guess = int(input("Enter your guess: "))

#Declared a global variable and intialized it with value 0, which will count the users number of guess in the while loop.
users_no_of_guess = 0

# Defining a guess fuction which will reply to users guess.
def guess(user_guess, compilers_guess):

    #For repetitive guessing, a while loop will be initialized.
    while user_guess != compilers_guess:
        

        #If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
        if user_guess > compilers_guess:
            print("Try again! You guessed too high")

        #Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
        elif user_guess < compilers_guess:
            print("Try again! You guessed too low")

        #Global variable is used here to count the users number of case.
        global users_no_of_guess
        users_no_of_guess += 1

        #Taking input from user for the further guessing.
        user_guess = int(input("Enter your guess: "))
        

        # You can comment out below line to get the users no of guess after each guess.
        #print(users_no_of_guess)


#Calling the guess function, while passing parameter user guess and compilers guess
guess(user_guess, compilers_guess)    




minimum_number_of_guessing = int(m.log(upper_bound - lower_bound + 1, 2))


if users_no_of_guess == minimum_number_of_guessing:
    print("Congratulations you did it in ",users_no_of_guess, " try")

elif users_no_of_guess > minimum_number_of_guessing:
    print("You had too many tries. Your number of tries: ", users_no_of_guess)

else:
    print("congrats you did it too fast. Your number of tries: ", users_no_of_guess)      
 

