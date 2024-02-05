# Import necessary libraries
import random

# Define the game board as a 2D list
game_board = [
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
]

# Define the tetromino shapes as 2D lists
# Each shape is represented by a different letter
# 'I' shape
I_shape = [
    ['-', '-', '-', '-'],
    ['I', 'I', 'I', 'I'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-']
]

# 'J' shape
J_shape = [
    ['J', '-', '-'],
    ['J', 'J', 'J'],
    ['-', '-', '-']
]

# 'L' shape
L_shape = [
    ['-', '-', 'L'],
    ['L', 'L', 'L'],
    ['-', '-', '-']
]

# 'O' shape
O_shape = [
    ['O', 'O'],
    ['O', 'O']
]

# 'S' shape
S_shape = [
    ['-', 'S', 'S'],
    ['S', 'S', '-'],
    ['-', '-', '-']
]

# 'T' shape
T_shape = [
    ['-', 'T', '-'],
    ['T', 'T', 'T'],
    ['-', '-', '-']
]

# 'Z' shape
Z_shape = [
    ['Z', 'Z', '-'],
    ['-', 'Z', 'Z'],
    ['-', '-', '-']
]

# Create a list of all the tetromino shapes
tetromino_shapes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]

# Generate a random index to select a shape from the list
random_index = random.randint(0, len(tetromino_shapes) - 1)

# Select a random shape from the list
random_shape = tetromino_shapes[random_index]

# Place the shape at the top of the game board
# The shape will be placed at the center of the top row
# Calculate the starting column index for the shape
start_col = (len(game_board[0]) - len(random_shape[0])) // 2

# Place the shape on the game board
for row in range(len(random_shape)):
    for col in range(len(random_shape[0])):
        game_board[row][start_col + col] = random_shape[row][col]

# Print the game board with the random shape at the top
for row in game_board:
    print(row)