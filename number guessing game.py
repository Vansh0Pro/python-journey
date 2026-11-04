import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

i=1

while i <= 1000:
    guess = int(input(f"Attempt {i}: Make a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {secret_number}.")
        break

    i += 1


retry=input("Do you want to play again? (y/n): ").lower()
if retry == "y":
    secret_number = random.randint(1, 100)
    attempts = 0
    i = 1
    print("I'm thinking of a new number between 1 and 100. You have 10 attempts to guess it.")
else:
    print("Thanks for playing! Goodbye.")