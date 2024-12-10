def quickSortDriver(arr, low, high):
    if low < high:
        partition: int = partitionF(arr, low, high)
        quickSortDriver(arr, low, partition - 1)
        quickSortDriver(arr, partition + 1, high)


def partitionF(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def mergeSortDriver(arr, low, high):
    if low == high:
        return

    mid = (low + high) // 2

    mergeSortDriver(arr, low, mid)
    mergeSortDriver(arr, mid + 1, high)
    mergeArr(arr, low, mid, high)


def mergeArr(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = quickSortDriver(arr, 0, n - 1)
    print(arr)


main()
