# Sudoku Solver

This Python project implements a backtracking algorithm to solve Sudoku puzzles. The solver takes a 9x9 Sudoku board as input and recursively fills the empty cells with valid numbers until a solution is found.

## Features

- Solve any valid 9x9 Sudoku puzzle
- Backtracking algorithm to ensure finding a solution (if one exists)
- Formatted output for easy readability of the solved board

## Usage

1. Clone the repository or download the source code.
2. Open `sudoku_solver.py` in a Python environment.
3. Modify the `board` list at the beginning of the file with your Sudoku puzzle. Each row is represented as a list of 9 integers, where 0 represents an empty cell.
4. Run the script, and the solved Sudoku board will be printed to the console.

## Example

```python
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
