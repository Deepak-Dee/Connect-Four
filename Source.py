
import numpy as np


# Function for creating the board, Here statically the board is of size 6 X 7
def create_board():
    board = np.zeros((6, 7))
    return board


board = create_board()
print(board)  # Command to print the board
turn = 0  # By default the turn must start with player 1
game_over = False

while not game_over:
    if turn == 0:
        # Ask for player 1 input
        selection = int(input("Enter the selection for player 1 : "))

    else:
        # Ask for player 2 input
        selection = int(input("Enter the selection for player 2 : "))

    turn += 1
    turn %= 2