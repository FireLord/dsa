def upperBound(arr, x: int) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(upperBound(nums, k))

main()