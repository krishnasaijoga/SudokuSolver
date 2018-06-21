import copy
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
    file_name = os.path.join(os.path.dirname(sys.argv[0]), 'sample2.txt')
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


def is_complete(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


def find_empty_loc(board):
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == 0:
                return row_idx, col_idx


def find_possibilities(board, i, j):
    if board[i][j] != 0:
        return False
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
    return list(numbers)


def fill_obvious(board):
    while True:
        board_changed = False
        for i in range(0, 9):
            for j in range(0, 9):
                possibilities = find_possibilities(board, i, j)
                if possibilities.__len__() == 0:
                    raise RuntimeError("No Moves left")
                if possibilities.__len__() == 1:
                    board[i][j] = possibilities[0]
                    board_changed = True
        if not board_changed:
            return


def solve_sudoku(board):
    try:
        fill_obvious(board)
    except:
        return False

    print("After Filling obvious")
    print(" ")
    print(is_complete(board))
    print_board(board)
    print(" ")

    if is_complete(board):
        return True

    # i, j = 0, 0

    i, j = find_empty_loc(board)
    # for row_idx, row in enumerate(board):
    #     for col_idx, col in enumerate(row):
    #         if col == 0:
    #             i, j = row_idx, col_idx
    #             break
    possibilities = find_possibilities(board, i, j)

    if type(possibilities).__name__ == 'list':
        for value in possibilities:
            snapshot = copy.deepcopy(board)
            board[i][j] = value
            result = solve_sudoku(board)
            if result:
                return True
            else:
                board = copy.deepcopy(snapshot)
    return False


def sud_solve():
    board = read_board()
    solve_sudoku(board)
    print("Board Filled Completely")
    print(" ")
    print_board(board)


if __name__ == '__main__':
    sud_solve()
