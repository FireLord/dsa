def rotateImageOpt(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # transpose
    for i in range(n):
        for j in range(i+1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for i in range(n):
        matrix[i].reverse()


def rotateImage(matrix):
    n = len(matrix)
    m = len(matrix[0])
    newMatrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            newMatrix[j][(n - 1) - i] = matrix[i][j]

    return newMatrix


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateImageOpt(matrix)
    print(matrix)


main()
