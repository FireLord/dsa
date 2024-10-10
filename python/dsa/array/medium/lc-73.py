
def matrixZero(matrix):
    n = len(matrix)
    for i in range(n):
        m = len(matrix[i])
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(i, m, matrix)
                markCol(j, n, matrix)
    
    for i in range(n):
        m = len(matrix[i])
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
    matrix = [[-1],[2],[3]]
    print(matrixZero(matrix))

main()