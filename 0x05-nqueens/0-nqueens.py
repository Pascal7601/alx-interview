#!/usr/bin/python3
"""
a file that handles how backtracking works
in solving the N queens problem
"""
import sys


def solveNQueens(N: int):
    """
    base function to solve the N queens
    problem
    """
    posDiag = set() # r + c
    negDiag = set() # r - c
    col = set() # column where queen is located

    res = [] # result to return
    board = [["."] * N for i in range(N)]
    # return board


    def backtrack(r):
        """
        function that checks on where to place the
        queen and backtracks when there is no
        valid option
        """
        if r == N:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(N):
            if c in col or (r - c) in negDiag or (r + c) in posDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

if __name__ == '__main__':
    number = int(sys.argv[1])
    if not isinstance(number, int):
        print("N must be a number")
        exit(1)
    if number < 4:
        print("N must be at least 4")
        exit(1)
    
    print(solveNQueens(number))



# print(solveNQueens(4))
