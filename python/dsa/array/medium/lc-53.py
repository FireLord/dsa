# optimal
def maxSubArrayOpt(nums):
    n = len(nums)
    sumOfNums = 0
    maxSum = nums[0]

    for i in range(n):
        if sumOfNums < 0:
            sumOfNums = 0

        sumOfNums += nums[i]
        maxSum = max(maxSum, sumOfNums)

    return maxSum


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(maxSubArrayOpt(nums))


main()
