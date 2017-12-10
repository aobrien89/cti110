# A number guessing game between 1 and 100.
# 11/12/2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Anthony O'Brien
#
import random
def main():
    guessess = 5
    number = random.randint(1, 100)
    win = False
    while guessess > -1:
        guess = int(input("Guess: "))

        if guess > number:
            print("Your guess was too high, you have", guessess, "remaining")
        elif guess < number:
            print("Your guess was too low, you have", guessess, "remaining")
        else:
            print("Correct! You win!")
            win = True
        guessess -= 1
        
    if win == False:
            print("Sorry, you didnt guess the correct number. The correct number was " + str(number))
    restart = input("Do you want to play again? y for Yes n for No ").lower()
    
    if restart == "y":
        main()
    else:
        exit()

main()
