# optimal approach
def fourSumOptimal(nums, target):
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > 0 and nums[j] == nums[j-1]:
                continue

            k = j + 1
            l = n - 1
            while k < l:
                finalSum = nums[i] + nums[j]
                finalSum += nums[k]
                finalSum += nums[l]

                if finalSum < target:
                    k += 1
                elif finalSum > target:
                    l -= 1
                else:
                    tempArr = [nums[i], nums[j], nums[k], nums[l]]
                    result.append(tempArr)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1

    return result

# better approach
def fourSumBetter(nums, target):
    n = len(nums)
    result_set = set()

    for i in range(n):
        for j in range(i+1, n):
            uniqueElementSet = set()
            for k in range(j+1, n):
                fourthEle = target - nums[i] - nums[j] - nums[k]
                if fourthEle in uniqueElementSet:
                    tempArr = [nums[i], nums[j], nums[k], fourthEle]
                    tempArr.sort()
                    result_set.add(tuple(tempArr))
                uniqueElementSet.add(nums[k])

    result = list(result_set)
    return result

# Brute force approach
def fourSumBrute(nums, target):
    n = len(nums)
    result_set = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    finalSum = nums[i] + nums[j]
                    finalSum += nums[k]
                    finalSum += nums[l]
                    if finalSum == target:
                        tempArr = [nums[i], nums[j], nums[k], nums[l]]
                        tempArr.sort()
                        result_set.add(tuple(tempArr))

    result = list(result_set)
    return result


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(fourSumBrute(nums, n))
    print(fourSumBetter(nums, n))
    print(fourSumOptimal(nums, n))


main()
