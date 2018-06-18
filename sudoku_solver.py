import os
import sys


def read_board():
    board = []
    # print(sys.argv[0])    contains current working file pathname
    file_name = os.path.join(os.path.dirname(sys.argv[0]),'sample.txt')
    f = open(file_name, 'r')
    for x in f:
        temp = x.split()
        temp2 = []
        for each in temp:
            temp2.append(int(each))
            # if int(each) != 0:
            #     temp2.append([int(each), 1])    # permanent shouldn't be changed
            # else:
            #     temp2.append([int(each), 0])    # empty blocks, editable
        board.append(temp2)
    f.close()
    print_board(board)
    print()
    return board


def is_safe(board, row, col, num):
    if board[row].count(num) > 0:  # if num is present anywhere in the row
        return False
    for x in range(9):  # if num is present anywhere in the column
        if board[x][col] == num:
            return False
    # check for block safety
    block_row = (row / 3) * 3
    block_col = (col / 3) * 3
    for row_iter in range(block_row, block_row + 3):
        for col_iter in range(block_col, block_col + 3):
            if board[row_iter][col_iter] == num:
                return False
    return True
    pass


def find_free_loc(board, row, col):
    if board[row][col + 1:].count(0) > 0:
        if col != -1:
            return col + board[row][col + 1:].index(0) + 1
        else:
            return board[row][col + 1:].index(0)
    else:
        #   recurse back to previous stored num
        return 9
    pass


def fill_num(board, num):
    col = -1
    row = 0
    while 0 <= row < 9:
        if board[row].count(num) == 0:  # if num is not present in row
            col = find_free_loc(board, row, col)  # finding first free location in row from col index
            while col < 9:
                if col == 9:  # if no free location break
                    break
                if is_safe(board, row, col, num):  # check if location is safe
                    board[row][col] = num  # if safe place num in safe location and make col = 0
                    col = -1
                    break
                else:  # if location not safe find another
                    col = find_free_loc(board, row, col)
            if col == 9:
                row = row - 1
                if board[row].count(num) > 0:
                    col = board[row].index(num)
                    board[row][col] = 0
                    row = row - 1
        row = row + 1
    pass


def solve_sudoku(board):
    #   fill all 1's in board
    for num in range(1, 10):
        fill_num(board, num)  # TODO: From num = 2 it is entering infinite loop
    pass


def print_board(board):
    for row in range(9):
        print(board[row])
    pass


def sudoku_solver():
    #   read board from file
    board = read_board()
    #   solve sudoku
    solve_sudoku(board)
    #   print board
    print_board(board)
    pass


if __name__ == '__main__':
    sudoku_solver()
