# optimal
def threeSumOptimal(nums):
    n = len(nums)
    result = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            finalSum = nums[i] + nums[j] + nums[k]

            if finalSum < 0:
                j += 1
            elif finalSum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                result.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return result[::-1]


# better
def threeSumBetter(nums):
    n = len(nums)
    result_set = set()
    for i in range(n):
        uniqueElementSet = set()
        for j in range(i+1, n):
            thirdEle = -(nums[i] + nums[j])
            if thirdEle in uniqueElementSet:
                tempArr = [nums[i], nums[j], thirdEle]
                tempArr.sort()
                result_set.add(tuple(tempArr))

            uniqueElementSet.add(nums[j])

    result = list(result_set)
    return result


# brute force
def threeSum(nums):
    n = len(nums)
    result_set = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    tempArr = [nums[i], nums[j], nums[k]]
                    tempArr.sort()
                    result_set.add(tuple(tempArr))

    result = list(result_set)
    return result


def main():
    n = int(input())
    nums = [-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]
    print(threeSum(nums))
    print(threeSumBetter(nums))
    print(threeSumOptimal(nums))


main()
