import numpy as np

b1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
b2 = [
      [2, 0, 0, 0, 8, 0, 3, 0, 0],
      [0, 6, 0, 0, 7, 0, 0, 8, 4],
      [0, 3, 0, 5, 0, 0, 2, 0, 9],
      [0, 0, 0, 1, 0, 5, 4, 0, 8],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [4, 0, 2, 7, 0, 6, 0, 0, 0],
      [3, 0, 1, 0, 0, 7, 0, 4, 0],
      [7, 2, 0, 0, 4, 0, 0, 6, 0],
      [0, 0, 4, 0, 1, 0, 0, 0, 3]
]


def getEmptySqr(b):
    for row in range(len(b)):
        for col in range(len(b)):
            if b[row][col] == 0:
                return row, col

    return None


def validate(b, n, pos):
    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(len(b[0])):
        if b[pos[0]][i] == n and pos[1] != i:
            return False

    for i in range(len(b)):
        if b[i][pos[1]] == n and pos[0] != i:
            return False

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if b[i][j] == n and (i, j) != pos:
                return False
    return True


def solve(b):
    find = getEmptySqr(b)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if validate(b, i, (row, col)):
            b[row][col] = i
            if solve(b):
                return True
            b[row][col] = 0
    return False


print (np.matrix(b2))
print("solving...")
solve(b2)
print("Result:")
print (np.matrix(b2))
