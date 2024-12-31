#!/usr/bin/python3
"""
nqueens solution using backtracking
"""
import sys


def backtrack_algorithm(row, n, cols, pos_dgnal, neg_dgnal, board):
    """
    Recursively places queens on the board using backtracking
    Args:
        row (int): Current row to place a queen
        n (int): Size of the chessboard (N x N)
        cols (set): Columns where queens are placed
        pos_dgnal (set): Positive diagonals under attack
        neg_dgnal (set): Negative diagonals under attack
        board (list): Current state of the chessboard
    """
    if row == n:
        result = [
            [r, c] for r in range(n) for c in range(n) if board[r][c] == 1]
        print(result)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_dgnal or (row - col) in neg_dgnal:
            continue

        cols.add(col)
        pos_dgnal.add(row + col)
        neg_dgnal.add(row - col)
        board[row][col] = 1

        backtrack_algorithm(row + 1, n, cols, pos_dgnal, neg_dgnal, board)

        cols.remove(col)
        pos_dgnal.remove(row + col)
        neg_dgnal.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the N Queens problem
    Args:
        n (int): Number of queens | size of the chessboard
    """
    board = [[0] * n for _ in range(n)]
    backtrack_algorithm(0, n, set(), set(), set(), board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
