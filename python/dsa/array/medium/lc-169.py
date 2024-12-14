# optimal
# moore's voting algorithm
def majorityElementOpt(nums):
    n = len(nums)
    element = 0
    ctr = 0
    for i in range(n):
        if ctr == 0:
            ctr = 1
            element = nums[i]
        elif nums[i] == element:
            ctr += 1
        else:
            ctr -= 1

    for i in range(n):
        if nums[i] == element:
            ctr += 1

    if ctr > n // 2:
        return element
    else:
        return -1


# better
def majorityElement(nums):
    n = len(nums)
    countHash = {}
    for i in range(n):
        countHash[nums[i]] = countHash.get(nums[i], 0) + 1

    for key, value in countHash.items():
        if value > n // 2:
            return key

    return -1


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(majorityElementOpt(nums))


main()
