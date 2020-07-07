import numpy as np

R_COUNT = 6
C_COUNT = 7


# Function for creating the board, Here statically the board is of size 6 X 7
def create_board():
    board = np.zeros((R_COUNT, C_COUNT))
    return board


# Function for dropping a piece into the board
def piece_drop(board, row, col, piece):
    board[row][col] = piece


# Function to check for valid location
def valid_location(board, col):
    return board[5][col] == 0


# Function to check whether the next row is open for dropping a piece
def open_row(board, col):
    for r in range(R_COUNT):
        if board[r][col] == 0:
            return r


board = create_board()
print(board)
turn = 0  # By default the turn must start with player 1
game_over = False  # Loop variable

while not game_over:
    if turn == 0:
        # Ask for player 1 input
        col = int(input("Enter the selection for player 1 : "))

        if valid_location(board, col):
            row = open_row(board, col)
            piece_drop(board, row, col, 1)

    else:
        # Ask for player 2 input
        col = int(input("Enter the selection for player 2 : "))

        if valid_location(board, col):
            row = open_row(board, col)
            piece_drop(board, row, col, 2)

    print(board)
    turn += 1
    turn %= 2
