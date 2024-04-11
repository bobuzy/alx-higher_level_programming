#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n, result):
    """Recursive utility function to solve N-queens puzzle."""
    if row == n:
        result.append([[i, board[i].index('Q')] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n, result)
            board[row][col] = '.'

def solve_n_queens(n):
    """Solve the N-queens puzzle and return all solutions."""
    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    solve_n_queens_util(board, 0, n, result)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for sol in solutions:
        print(sol)
