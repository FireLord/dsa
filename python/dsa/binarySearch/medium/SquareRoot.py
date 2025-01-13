def squareRootBinary(n):
    ans = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        val = mid * mid
        if val <= n:
            # eliminate left half
            ans = mid
            low = mid + 1
        else:
            # eliminate right half
            high = mid - 1

    return ans

def squareRootLinear(n):
    ans = 0
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans


def main():
    k = int(input())
    print(squareRootLinear(k))
    print(squareRootBinary(k))


main()
