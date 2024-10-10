# optimal
def reArrangeSignOpt(nums):
    n = len(nums)
    positiveIndex = 0
    negativeIndex = 1
    result = [0] * n
    for i in range(n):
        if nums[i] >= 0:
            result[positiveIndex] = nums[i]
            positiveIndex += 2
        else:
            result[negativeIndex] = nums[i]
            negativeIndex += 2
    
    return result

# brute
def reArrangeSign(nums):
    n = len(nums)
    positiveNum = []
    negativeNum = []
    result = []
    for i in range(n):
        if nums[i] >= 0:
            positiveNum.append(nums[i])
        else:
            negativeNum.append(nums[i])
    
    positiveNum = positiveNum[::-1]
    negativeNum = negativeNum[::-1]

    for i in range(n):
        if i % 2 == 0:
            result.append(positiveNum.pop())
        else:
            result.append(negativeNum.pop())
    
    return result


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(reArrangeSignOpt(nums))

main()