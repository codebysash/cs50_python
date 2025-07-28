import random

number = random.randint(1, 100)

while True:
    guess_input = input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess_input)
    except ValueError:
        print("That's not a number! Pleae enter number between 1 and 100.")
        continue
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number")
        break