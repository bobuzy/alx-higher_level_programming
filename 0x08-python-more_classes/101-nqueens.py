#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def copy_board(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return [copy_board(row) for row in board]
    return board


def get_queen_positions(board):
    """Return the positions of queens on the board."""
    queens = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                queens.append([row, col])
    return queens


def mark_attacked_positions(board, row, col):
    """Mark attacked positions on the board."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_n_queens(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_queen_positions(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][col] = "Q"
            mark_attacked_positions(tmp_board, row, col)
            solutions = solve_n_queens(tmp_board, row + 1, queens + 1, solutions)

    return solutions


def main():
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

    chessboard = initialize_board(n)
    result_solutions = solve_n_queens(chessboard, 0, 0, [])
    for solution in result_solutions:
        print(solution)


if __name__ == "__main__":
    main()
