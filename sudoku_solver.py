import os
import random
import sys


def read_board():
    board = []
    # print(sys.argv[0])    contains current working file pathname
    file_name = os.path.join(os.path.dirname(sys.argv[0]), 'sample.txt')
    f = open(file_name, 'r')
    for x in f:
        temp = x.split()
        temp2 = []
        for each in temp:
            # temp2.append(int(each))
            if int(each) != 0:
                temp2.append([int(each), 1])    # permanent shouldn't be changed
            else:
                temp2.append([int(each), 0])    # empty blocks, editable
        board.append(temp2)
    f.close()
    print_board(board)
    print('')
    return board


def is_safe(board, row, col, num):
    if board[row].count([num, 1]) > 0 or board[row].count([num, 0]) > 0:  # if num is present anywhere in the row
        return False
    for x in range(9):  # if num is present anywhere in the column
        if board[x][col] == [num, 0] or board[x][col] == [num, 1]:
            return False
    # check for block safety
    block_row = (row / 3) * 3
    block_col = (col / 3) * 3
    for row_iter in range(block_row, block_row + 3):
        for col_iter in range(block_col, block_col + 3):
            if board[row_iter][col_iter] == [num, 1] or board[row_iter][col_iter] == [num, 0]:
                return False
    return True
    pass


def find_free_loc(board, row, col):
    if board[row][col + 1:].count([0, 0]) > 0:
        if col != -1:
            return col + board[row][col + 1:].index([0, 0]) + 1
        else:
            return board[row][col + 1:].index([0, 0])
    else:
        #   recurse back to previous stored num
        return 9
    pass


def fill_num(board, num):
    col = -1
    row = 0
    while 0 <= row < 9:
        if board[row].count([num, 1]) == 0 and board[row].count([num, 0]) == 0:  # if num is not present in row
            col = find_free_loc(board, row, col)  # finding first free location in row from col index
            while col < 9:
                if col == 9:  # if no free location break
                    break
                if is_safe(board, row, col, num):  # check if location is safe
                    board[row][col] = [num, 0]  # if safe place num in safe location and make col = 0
                    col = -1
                    break
                else:  # if location not safe find another
                    col = find_free_loc(board, row, col)
            if col == 9:
                row = row - 1
                while row != -1 and board[row].count([num, 1]) > 0:
                    row = row - 1
                else:
                    if row < 0:
                        return False
                    if board[row].count([num, 0]) > 0:
                        col = board[row].index([num, 0])
                        board[row][col] = [0, 0]
                        row = row - 1
        row = row + 1
    if row == 9:
        return True
    return False
    pass


prev_num = 0


def fill_board(board, nums):
    global prev_num
    if nums.__len__() == 0:
        return True
    num = random.choice(nums)
    if fill_num(board, num):
        nums.pop(nums.index(num))
        prev_num = num
        fill_board(board, nums)
    else:
        nums.append(prev_num)
        fill_board(board, nums)
    pass


def solve_sudoku(board):
    #   fill all 1's in board
    nums = list(range(1, 10))

    fill_board(board, nums)

    # while nums.__len__() > 0:
    #     num = random.choice(nums)
    #     nums.pop(nums.index(num))
    #     fill_num(board, num)

    # while num < 10:
    #     if fill_num(board, num):
    #         num = num + 1
    #     else:
    #         num = num - 1
    pass


def print_board(board):
    for row in range(0, 9):
        if row != 0 and row % 3 == 0:
            print('------+-------+-------')
        for col in range(0, 9):
            if col != 0 and col % 3 == 0:
                print('|'),
            print(board[row][col][0]),  # ',' to print next in same line
        print(' ')
    pass


def sudoku_solver():
    #   read board from file
    board = read_board()
    #   solve sudoku
    try:
        solve_sudoku(board)
    except RuntimeError as re:
        print("This board cannot be solved")
    #   print board
    print_board(board)
    pass


if __name__ == '__main__':
    sudoku_solver()
