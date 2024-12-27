def missingNumOptimal(nums):
    n = len(nums)
    # sumNum - sumNaturalNum = repeatingNum - missingNum
    # s2 - s2n
    sumNaturalNum = (n * (n+1)) // 2
    squareNaturalNum = (n * (n+1) * (2*n+1)) // 6
    sumNum = 0
    squareNum = 0

    for i in range(n):
        sumNum += nums[i]
        squareNum += nums[i] * nums[i]

    eq1 = sumNum - sumNaturalNum
    eq2 = squareNum - squareNaturalNum
    eq2 = eq2 // eq1
    repeatingNum = (eq1 + eq2) // 2
    missingNum = repeatingNum - eq1

    return [repeatingNum, missingNum]


def missingNumBetter2(nums):
    n = len(nums)
    hash = [0] * (n + 1)

    for i in range(n):
        hash[nums[i]] += 1

    repeatingNum = -1
    missingNum = -1

    for i in range(1, n + 1):
        if hash[i] == 2:
            repeatingNum = i
        elif hash[i] == 0:
            missingNum = i

        if repeatingNum != -1 and missingNum != -1:
            break
    return [repeatingNum, missingNum]

def missingNumBetter1(nums):
        n = len(nums)
        hashData = {}
        result = [-1, -1]
        
        for i in range(1, n+1):
            hashData[i] = 0
        
        for item in nums:
            hashData[item] = hashData.get(item, 0) + 1
        
        for key, value in hashData.items():
            if value == 2:
                result[0] = key
            elif value == 0:
                result[1] = key

        return result

def missingNumBrute(nums):
    n = len(nums)
    missingNum = float("-inf")
    repeatingNum = float("-inf")

    for i in range(1, n+1):
        ctr = 0
        for j in range(n):
            if nums[j] == i:
                ctr += 1
        if ctr == 2:
            repeatingNum = i
        elif ctr == 0:
            missingNum = i

        if missingNum != float("-inf") and repeatingNum != float("-inf"):
            break

    return [repeatingNum, missingNum]


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(missingNumBrute(nums))
    print(missingNumBetter1(nums))
    print(missingNumBetter2(nums))
    print(missingNumOptimal(nums))


main()
