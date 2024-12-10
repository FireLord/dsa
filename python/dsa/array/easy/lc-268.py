def missingNumXor():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    n = len(nums)
    xor1 = 0
    xor2 = 0
    
    for i in range(n):
        xor2 = xor2 ^ nums[i]
        xor1 = xor1 ^ (i+1)
    
    print (xor1 ^ xor2)


def missingNumSum():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    sumOfNumsActual = sum(nums)
    sumOfNumsExpected = 0
    for i in range(len(nums) + 1):
        sumOfNumsExpected += i

    print(sumOfNumsExpected - sumOfNumsActual)


def missingNum():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    n = len(nums)
    nums.sort()
    for i in range(n):
        if i != nums[i]:
            print(i)


# missingNum()
missingNumSum()
missingNumXor()