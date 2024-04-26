
import random

print("Welcome", "\nGoodluck for the game\n You need to guess the brand names.\n  ")

word = ('dell','lenovo','asus','hp','vivo','oppo','redmi','samsung')
random_word = random.choice(word)
print("Guess a brand name with ", len(random_word), "letters.")
guesses = ''
hearts = 10

while hearts > 0:

    failed = 0
    for char in random_word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_")
            failed+=1

    if failed == 0:
        print('You Win')
        print("The word is: ", random_word)
    print()
    guess = input("Enter Your guess: ")
    guesses += guess

    if guess not in random_word:
        hearts -= 1
        print("Wrong")
        print("You have", + hearts, 'more guesses')
 
        if hearts == 0:
            print("You Loose")
