# best solution
def majorityEleBest(nums):
    n = len(nums)
    ctr1 = 0
    ctr2 = 0
    ele1 = float("-inf")
    ele2 = float("-inf")
    result = []

    for i in range(n):
        if ctr1 == 0 and ele2 != nums[i]:
            ctr1 = 1
            ele1 = nums[i]
        elif ctr2 == 0 and ele1 != nums[i]:
            ctr2 = 1
            ele2 = nums[i]
        elif nums[i] == ele1:
            ctr1 += 1
        elif nums[i] == ele2:
            ctr2 += 1
        else:
            ctr1 -= 1
            ctr2 -= 1

    ctr1 = 0
    ctr2 = 0

    for i in range(n):
        if ele1 == nums[i]:
            ctr1 += 1
        if ele2 == nums[i]:
            ctr2 += 1

    minimum = (n//3) + 1
    if ctr1 >= minimum:
        result.append(ele1)

    if ctr2 >= minimum:
        result.append(ele2)

    result.sort()
    return result


# better solution
def majorityEleBetter(nums):
    result = []
    hash = {}
    minimum = (len(nums) // 3) + 1
    for i in range(len(nums)):
        hash[nums[i]] = hash.get(nums[i], 0) + 1
        if hash[nums[i]] == minimum:
            result.append(nums[i])

    return result


# brute force
def majorityEle(nums):
    n = len(nums)
    result = []

    for i in range(n):
        if len(result) == 0 or result[0] != nums[i]:
            ctr = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    ctr += 1

            if ctr > (n//3):
                result.append(nums[i])

        if len(result) == 2:
            break

    return result


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(majorityEle(nums))
    print(majorityEleBetter(nums))
    print(majorityEleBest(nums))


main()
