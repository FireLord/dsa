def matrixZeroOpt(matrix):
    n = len(matrix)
    m = len(matrix[0])



def matrixZeroBetter(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col = [0] * m
    row = [0] * n

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    
    return matrix


def matrixZero(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):    
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(i, m, matrix)
                markCol(j, n, matrix)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix

def markRow(i, m, matrix):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(j, n, matrix):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def main():
    n = int(input())
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(matrixZeroOpt(matrix))

main()