import numpy as np


# Function for creating the board, Here statically the board is of size 6 X 7
def create_board():
    board = np.zeros((6, 7))
    return board


board = create_board()
print(board)