def singleNonDuplicateBinary(nums):
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


main()
