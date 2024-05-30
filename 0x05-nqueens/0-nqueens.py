#!/usr/bin/python3
"""0x05. N Queens"""

import sys


def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(0)
        board.append(row)
    return board


def safe_place(board, col, row, N):
    """check is safe place for the queen"""
    for i in range(col):
        if (board[row][i] == 1):
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_it(board, N, col, solutions):
    """THIS IS THE function that can solve the probleme"""
    if (col >= N):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(N):
        if safe_place(board, col, i, N):
            board[i][col] = 1
            if (solve_it(board, N, col + 1, solutions) is True):
                return True
            board[i][col] = 0
    return False


def n_queens(N: int):
    """the function that solve the probleme"""
    board = create_board(N)
    solutions = []
    solve_it(board, N, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """the main of the program"""
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens(num)
