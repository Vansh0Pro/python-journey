import random

#1=scisors
#2=paper
#3=rock

computer_choice = random.randint(1, 3)

print("----------------------------------------------------------------------------------------------------------")
print("Welcome to Rock, Paper, Scissors!")
print("The computer has chosen its move.")
print("Your turn to choose!")
user_choice = int(input("Enter 1 for Scissors, 2 for Paper, or 3 for Rock:"))

if user_choice == 1:
    print("You chose Scissors.")
elif user_choice == 2:
    print("You chose Paper.")
elif user_choice == 3:
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

if user_choice == 1 and computer_choice == 2:
    result = "You win! Scissors beats Paper."
elif user_choice == 1 and computer_choice == 3:
    result = "You lose! Scissors beats Paper."
elif user_choice == 2 and computer_choice == 1:
    result = "You lose! Paper beats Scissors."
elif user_choice == 2 and computer_choice == 3:
    result = "You win! Rock beats Paper."
elif user_choice == 3 and computer_choice == 1:
    result = "You win! Rock beats Scissors."
elif user_choice == 3 and computer_choice == 2:
    result = "You lose! Rock beats Scissors."
else:
    result = "It's a tie!"

print(result)
