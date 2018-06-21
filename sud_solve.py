import os
import sys


def print_board(board):
    for row in range(0, 9):
        if row != 0 and row % 3 == 0:
            print('------+-------+-------')
        for col in range(0, 9):
            if col != 0 and col % 3 == 0:
                print('|'),
            print(board[row][col]),  # ',' to print next in same line
        print(' ')


def read_board():
    board = []
    # print(sys.argv[0])    contains current working file pathname
    file_name = os.path.join(os.path.dirname(sys.argv[0]), 'sample.txt')
    f = open(file_name, 'r')
    for x in f:
        temp = x.split()
        temp2 = []
        for each in temp:
            temp2.append(int(each))  # empty blocks, editable
        board.append(temp2)
    f.close()
    print_board(board)
    print('')
    return board


def find_possibilities(board, i, j):
    numbers = {x for x in range(1, 10)}
    for x in board[i]:
        numbers = numbers - {x}
    for x in range(0, 9):
        numbers = numbers - {board[x][j]}
    row_i = (i / 3) * 3
    col_j = (j / 3) * 3
    for x in range(row_i, row_i + 3):
        for y in range(col_j, col_j + 3):
            numbers = numbers - {board[x][y]}
    if numbers.__len__() == 0:
        return False
    return numbers
    pass


def count_of_values_in_board(board):
    count = 0
    for row in board:
        for col in row:
            if col != 0:
                count = count + 1
    return count


def fill_obvious(board):
    count = count_of_values_in_board(board)
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                possibilities = find_possibilities(board, i, j)
                if not possibilities:
                    return
                if possibilities.__len__() == 1:
                    board[i][j] = possibilities.pop()
                    count = count + 1
    if count != 81:
        fill_obvious(board)


def sud_solve():
    board = read_board()

    try:
        fill_obvious(board)
    except RuntimeError as re:
        print("This board can't be solved")

    print_board(board)
    pass


if __name__ == '__main__':
    sud_solve()
