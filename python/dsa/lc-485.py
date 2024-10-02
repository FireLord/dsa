
def maxOnes(nums):
    n = len(nums)
    oneTempCount = 0
    consecutiveOne = 0
    for i in range(n):
        if nums[i] == 1:
            oneTempCount += 1
            consecutiveOne = max(consecutiveOne, oneTempCount)
        else:
            oneTempCount = 0
    
    return consecutiveOne

def main():
    nums = [int(x) for x in input().split()]
    print(maxOnes(nums))

main()