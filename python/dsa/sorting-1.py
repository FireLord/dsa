def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while (j > 0) and (arr[j - 1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        # swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                # swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # if swapped != True:
        #     break
        # print("runs")
        # ^ optimal approach
    # time complexity - avg/worst - n2
    #                   best - n for already sorted
    return arr


def selectionSort(arr):
    # time complexity - n2 for all
    size = len(arr)

    for i in range(size):
        mini = i
        for j in range(i, size):
            if arr[j] < arr[mini]:
                mini = j

        arr[mini], arr[i] = arr[i], arr[mini]

    return arr


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = insertionSort(arr)
    print(result)


main()
