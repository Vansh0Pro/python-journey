import random

# Generate a random number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. u have 10 attempts to guess it.")

# Your code starts here 👇

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

guess = int(input("Make a guess: "))
print(f"You guessed: {guess}")

if guess == secret_number:
    print("Congratulations! You guessed the number!")
else:
    print("nope, thats a bit too " + ("high" if guess > secret_number else "low") + ".")

print("Game over! You've used all your attempts.")
print(f"The secret number was: {secret_number}")