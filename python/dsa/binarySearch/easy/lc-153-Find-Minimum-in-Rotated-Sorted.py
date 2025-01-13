import sys


def findMinBinary(nums, k):
    n = len(nums)
    low = 0
    high = n - 1
    ans = sys.maxsize
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans


def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(findMinBinary(nums, k))


main()
