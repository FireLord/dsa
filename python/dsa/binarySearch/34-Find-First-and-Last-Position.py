def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def searchRangeBinary(nums, target):
    n = len(nums)
    lowerBoundValue = lowerBound(nums, target)
    if lowerBoundValue == n or nums[lowerBoundValue] != target:
        return [-1, -1]
    upperBoundValue = upperBound(nums, target) - 1
    return [lowerBoundValue, upperBoundValue]


def main():
    target = int(input())
    nums = [int(x) for x in input().split(",")]
    print(searchRangeBinary(nums, target))


main()
