def waysToSplitArrayBrute(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(nums[:i-1]) > 0 and len(nums[j:n]) > 0:
                firstSum = sum(nums[:i])
                secondSum = sum(nums[j:n])
                if firstSum >= secondSum:
                    count += 1
                    break
    return count


def main():
    nums = [int(x) for x in input().split(",")]
    print(waysToSplitArrayBrute(nums))


main()