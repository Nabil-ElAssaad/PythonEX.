import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry, Guess again , too low")
        elif guess > random_number:
            print("Sorry, Guess again , too high")
    print("Yay you have guessed the number " , random_number , " correctlly!!")

def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high:
        guess = random.randint(low,high)
        feedback = input(f" is {guess} too high (H), too low (L) , or correct (c) ?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print("Yay The Computer has guessed the number ", guess, " correctly!!")


