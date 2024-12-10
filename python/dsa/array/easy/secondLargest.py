# better sol - 2n
def getSecondLargest(arr):
    n = len(arr)
    maxVal = max(arr)  # time complexity - 0(n)
    secondLargest = -1
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != maxVal:
            secondLargest = arr[i]
    return secondLargest


def getSecondLargestOpt(arr):
    n = len(arr)
    largest = arr[0]
    secondLargest = -1
    for i in range(n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(getSecondLargestOpt(arr))


main()
