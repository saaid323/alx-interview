#!/usr/bin/python3
import sys


def is_safe(board, row, col, n_1):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n_1 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(n_2):
    board = [[0] * n_2 for _ in range(n_2)]
    solutions = []

    def backtrack(col):
        if col == n_2:
            solution = []
            for i in range(n_2):
                for j in range(n_2):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for row in range(n_2):
            if is_safe(board, row, col, n_2):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)

    return solutions


def print_solutions(n_3):
    solutions = solve_nqueens(n_3)
    for solution in solutions:
        print(solution)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
print_solutions(int(N))
