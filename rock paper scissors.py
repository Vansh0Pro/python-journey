import random
computer_choice = random.randint(1, 3)

#1=scisors
#2=paper
#3=rock

up= 0
cp= 0

print("----------------------------------------------------------------------------------------------------------")
print("Welcome to Rock, Paper, Scissors!")
print("The computer has chosen its move.")
print("Your turn to choose!")
user_choice = input("Enter 1 for Scissors, 2 for Paper, or 3 for Rock:")

if user_choice == "1":
    print("You chose Scissors.")
elif user_choice == "2":
    print("You chose Paper.")
elif user_choice == "3":
    print("You chose Rock.")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    exit()

if computer_choice == 1:
    print("The computer chose Scissors.")
elif computer_choice == 2:
    print("The computer chose Paper.")
elif computer_choice == 3:
    print("The computer chose Rock.")

if user_choice == "1" and computer_choice == 2:
    result = "W"
elif user_choice == "1" and computer_choice == 3:
    result = "L"
elif user_choice == "2" and computer_choice == 1:
    result = "L"
elif user_choice == "2" and computer_choice == 3:
    result = "W"
elif user_choice == "3" and computer_choice == 1:
    result = "W"
elif user_choice == "3" and computer_choice == 2:
    result = "L"
else:
    result = "T"

if result == "W":
    print("You win!")
    up= +1
elif result == "L":
    print("You lose!")
    cp= -1
elif result == "T":
    print("It's a tie!")
print("Your current points:", up)
print("Computer current points:", cp)

print("do u want to play again?")
if input().lower() == "y":
    print("Starting a new round...")
else:
    print("Thanks for playing!")

