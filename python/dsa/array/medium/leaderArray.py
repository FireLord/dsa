# optimal
def leaderArrayOpt(arr):
    n = len(arr)
    maxEle = 0
    result = []
    for i in range(n-1,-1,-1):
        if arr[i] > maxEle:
            result.append(arr[i])
        maxEle = max(maxEle, arr[i])
    result.reverse()

    return result


# brute
def leaderArray(arr):
    n = len(arr)
    result = []
    for i in range(n):
        leader = True
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                leader = False
                break
            
        if leader == True:
            result.append(arr[i])

    return result


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(leaderArrayOpt(nums))


main()
