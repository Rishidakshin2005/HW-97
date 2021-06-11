import random

number= random.randrange(1,50)
guess = int (input("Guess a number between 1 and 100:"))

while guess!=number:
    if guess<number:
        print("You need to guess higher. Try Again")
        guess = int (input("Guess a number between 1 and 100:"))
else:
    print("You need to guess lower.Try Again")
    guess = int(input("Guess a number between 1 and 100:"))

    print("You guessed number correctly")
