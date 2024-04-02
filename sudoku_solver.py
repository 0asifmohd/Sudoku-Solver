"""
Sudoku Solver

This Python script implements a backtracking algorithm to solve Sudoku puzzles.
It takes a 9x9 Sudoku board as input and finds a valid solution by recursively
filling empty cells with valid numbers.

Author: Asif Muhammad Naseer
"""

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):
    """
    Solves the Sudoku puzzle using a backtracking algorithm.

    Args:
        bo (list): A 9x9 list representing the Sudoku board.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

        return False

def find_empty(bo):
    """
    Finds the first empty cell in the Sudoku board.

    Args:
        bo (list): A 9x9 list representing the Sudoku board.

    Returns:
        tuple: The row and column indices of the first empty cell, or None if no empty cells are found.
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

def valid(bo, num, pos):
    """
    Checks if a number can be placed in a specific cell on the Sudoku board.

    Args:
        bo (list): A 9x9 list representing the Sudoku board.
        num (int): The number to be checked.
        pos (tuple): The row and column indices of the cell to be checked.

    Returns:
        bool: True if the number can be placed in the cell, False otherwise.
    """
    # Check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 sub-grid
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):
    """
    Prints the Sudoku board in a formatted way.

    Args:
        bo (list): A 9x9 list representing the Sudoku board.
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# Solve the Sudoku puzzle
solve(board)

# Print the solution
print_board(board)
