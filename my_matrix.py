import random

def printMatrix(n, m):
    n = int(n)
    m = int(m)
    matrix = [[random.randint(20, 80) for _ in range(m)] for _ in range(n)]
    for row in matrix:
        print(row)
    print('------------')