slot1= "a"
slot2= "b"
slot3= "c"
slot4= "d"
slot5= "e"
slot6= "f"
slot7= "g"
slot8= "h"
slot9= "i"

player1= "x"
player2= "o"

print("Welcome to Tic Tac Toe!")
print("Player 1 is 'x' and Player 2 is 'o'")
print("The board is numbered as follows:")
print(f"{slot1} | {slot2} | {slot3}")
print(f"{slot4} | {slot5} | {slot6}")
print(f"{slot7} | {slot8} | {slot9}")
move1 = input("To make a move, enter the letter corresponding to the slot you want to mark: ")

after1 = slot1.replace(move1, player1)


