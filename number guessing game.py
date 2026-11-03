import random

# Generate a random number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. u have 10 attempts to guess it.")

# Your code starts here 👇

i=1

while i <= 10:
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