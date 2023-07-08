#!/usr/bin/python3

import sys

"""
This program implements the backtrack
algorithm to solve the N queens problem
"""


def main():
    """
    This function starts the program by checking argv
    and callling the solveNqueens function

    It prints the solution when the solveNqueens program returns
    """

    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_size = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)

    if n_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    all_solutions = []
    board = [[0 for i in range(n_size)] for j in range(n_size)]

    solveNqueens(0, 0, board, all_solutions, n_size)

    for soln in all_solutions:
        print(soln)


def solveNqueens(row, col, board, ans, n):

    """
    This function implements backtracking to solve the N queens problem.
    It uses recursion to implement backtracking

    Args:
        row(:object:`list`): The current row to be checked
        col(:object:`list`): The current col to be checked
        board(:object:`list`): List of list to store chessboard state
        ans(:object:`list`): List of list to hold all solutions
        n(:object:`int`): The size of the chessboard

    Description:
        This function first starts at the first row of board.

        It then loops through every available column in that row to see
        if a queen can be placed there.

        For current column, if we find a row where queen can be placed,
        put queen there and check if a solution exists
        there by recursively calling the function again whilst advancing the
        row being checked.

        If queen cannot be placed, advance to next column of row and
        repeat above 2 paragraphs.

        If all rows have been checked (row == n), store current board state
        as solution, return from recursion and backtrack (board[row][col] = 0).

    """
    # Base case
    if row == n:
        add_solution(ans, board)
        return

    for col in range(n):
        # Check if queen placing is valid in current square
        if isValidMove(board, row, col, n):
            board[row][col] = 1
            solveNqueens(row + 1, col, board, ans, n)

            # Backtrack
            board[row][col] = 0


def add_solution(answer, board):
    """
    This function takes the current board state and storees it
    as a solution to the n queens problem in the answer list.

    Args:
        board(:object:`list`): List of list to store chessboard state
        answer(:object:`list`): List of list to hold all solutions

    """
    single_answer = []
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if (row[j]):
                single_answer.append([i, j])

    answer.append(single_answer)


def isValidMove(board, row, col, n):
    """
    This function implements backtracking to solve the N queens problem.
    It uses recursion to implement backtracking

    Args:
        board(:object:`list`): List of list to store chessboard state
        row(:object:`list`): The current row to be checked
        col(:object:`list`): The current col to be checked
        n(:object:`int`): The size of the chessboard

    Description:
        This function checks if a queen can be placed in a given square
        with coords (row, col) in `board` of size `n`

    """
    if (1 in board[row]):
        return False

    for i in range(n):
        if board[i][col]:
            return False

    # For left diagonal
    x = row
    y = col

    # Setting coords leftmost diagonal square
    # This loop advances coord (x,y) to leftmost diagonal square
    # of coord (row, col)
    while (x > 0 and y > 0):
        if board[x][y]:
            return False
        x -= 1
        y -= 1

    # This loops moves down the left diagonal and checks
    # that there is no queen there
    while (x < n and y < n):
        if board[x][y]:
            return False
        x += 1
        y += 1

    # For right diagonal
    x = row
    y = col

    # Setting coords to rightmost diagonal square
    while (x > 0 and y < n-1):
        if board[x][y]:
            return False
        x -= 1
        y += 1

    # Moving down diagonal
    while (x < n and y >= 0):
        if board[x][y]:
            return False
        x += 1
        y -= 1

    return True


main()
