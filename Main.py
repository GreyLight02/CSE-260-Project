from z3 import *


def display(board):
    for i in range(len(board)):
        print(board[i])


def intialize():
    n = int(input("Please input an int: "))
    board = []
    for i in range(n):
        temp = []
        for x in range(n):
            temp.append(0)
        board.append(temp)

    return board

def main():

    mySolver = Solver()

    board = intialize()

#################################


#Our code goes here













#################################


if __name__ == "__main__":
    main()
