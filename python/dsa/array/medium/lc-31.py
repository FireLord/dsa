def nextGreaterPermutation(nums):
    n = len(nums)
    breakpoint = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            breakpoint = i
            break

    if breakpoint == -1:
        nums.reverse()
        return nums

    for i in range(n - 1, breakpoint, -1):
        if nums[i] > nums[breakpoint]:
            nums[i], nums[breakpoint] = nums[breakpoint], nums[i]
            break

    nums[breakpoint + 1 :] = reversed(nums[breakpoint + 1 :])
    return nums


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(nextGreaterPermutation(nums))


main()
