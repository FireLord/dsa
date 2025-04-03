def singleNonDuplicateBinary(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    low = 1
    high = n - 2
    while (low <= high):
        mid = (low + high) // 2
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
            return nums[mid]

        # we are in left
        if mid % 2 == 1 and nums[mid] == nums[mid - 1] or mid % 2 == 0 and nums[mid] == nums[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def singleNonDuplicateLinear(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    for i in range(n):
        # Check for first index
        if i == 0:
            if nums[i] != nums[i + 1]:
                return nums[i]
        # Check for last index
        elif i == n - 1:
            if nums[i] != nums[i - 1]:
                return nums[i]
        else:
            # we are checking if any side has the same value, if not then that's the ans
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
    return -1


def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(singleNonDuplicateLinear(nums))
    print(singleNonDuplicateBinary(nums))


main()
