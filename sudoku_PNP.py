import numpy as np
import copy

def basic(sudoku):
    temp = []
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sudoku[i][j])
        temp = checkArray(temp)
        for j in range(9):
            sudoku[i][j] = temp[j]

    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sudoku[j][i])
        temp = checkArray(temp)
        for j in range(9):
            sudoku[j][i] = temp[j]

    checkBox(sudoku, 0, 0)
    checkBox(sudoku, 0, 3)
    checkBox(sudoku, 0, 6)
    checkBox(sudoku, 3, 0)
    checkBox(sudoku, 3, 3)
    checkBox(sudoku, 3, 6)
    checkBox(sudoku, 6, 0)
    checkBox(sudoku, 6, 3)
    checkBox(sudoku, 6, 6)


def checkArray(row):
    cnt = 0
    l = [i for i in range(1, 10)]

    for j in range(len(row)):
        if row[j] == 0:
            cnt += 1
        else:
            l.remove(row[j])
        if cnt > 1:
            break

    if len(l) == 1:
        row[row.index(0)] = l[0]

    return row


def checkBox(sudoku, row, col):
    l = getBox(sudoku, row, col)
    if len(l) == 1:
        row = (int(row/3)*3)
        col = (int(col/3)*3)

        for r in range(3):
            for c in range(3):
                if sudoku[row+r][col+c] == 0:
                    sudoku[row+r][col+c] = l[0]


def getBox(sudoku, row, col):
    l = [i for i in range(1, 10)]
    row = (int(row/3)*3)
    col = (int(col/3)*3)

    for r in range(3):
        for c in range(3):
            if sudoku[row+r][col+c] != 0:
                l.remove(sudoku[row+r][col+c])
    return l


def getRow(sudoku, row):
    l = [i for i in range(1, 10)]

    for col in range(9):
        if sudoku[row][col] != 0:
            l.remove(sudoku[row][col])
    return l


def getCol(sudoku, col):
    l = [i for i in range(1, 10)]

    for row in range(9):
        if sudoku[row][col] != 0:
            l.remove(sudoku[row][col])
    return l


def singleNaked(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                l1 = getRow(sudoku, i)
                l2 = getCol(sudoku, j)
                l3 = getBox(sudoku, i, j)

                tmp = []
                for m in range(9):
                    if ((m+1) in l1) and ((m+1) in l2) and ((m+1) in l3):
                        tmp.append(m+1)
                    if len(tmp) == 1:
                        sudoku[i][j] = tmp[0]


def complete(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True


def sudoku_solver(sudoku):
    a = copy.deepcopy(sudoku)
    for h in range(10):
        print("h: ", h)
        if complete(sudoku):
            break
        tmp = copy.deepcopy(a)
        singleNaked(a)
        # basic(sudoku)
        if np.array_equal(tmp, a):
            break
    
    return a
