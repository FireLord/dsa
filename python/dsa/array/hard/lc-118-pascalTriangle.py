# optimal whole pascal triangle
def pascalTriangleOpt(n):
    result = []
    for i in range(1, n+1):
        arr = rowEleOpt(i)
        result.append(arr)
    return result

# brute whole pascal triangle
def pascalTriangle(n):
    result = []
    for i in range(1, n+1):
        arr = rowEle(i)
        result.append(arr)
    return result

# optimal for row elements
def rowEleOpt(n):
    arr = []
    ans = 1
    arr.append(ans)

    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // i
        arr.append(ans)

    return arr

# brute force to print row elements
def rowEle(n):
    arr = []
    for i in range(1, n+1):
        arr.append(ncr(n-1, i-1))
    return arr


def ncr(n, r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res


def main():
    n = int(input())
    print(rowEle(n))
    print(rowEleOpt(n))
    print(pascalTriangle(n))
    print(pascalTriangleOpt(n))


main()
