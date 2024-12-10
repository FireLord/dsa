# better
def twoSumBetter(nums, target):
    n = len(nums)
    hash = {}
    positions = []
    for i in range(n):
        a = nums[i]
        more = target - a
        if more in hash:
            positions.append(i)
            positions.append(hash[more])
        hash[a] = i

    return positions


# brute force
def twoSum(nums, k):
    n = len(nums)
    positions = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == k:
                positions.append(i)
                positions.append(j)
                break
    return positions


def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(twoSumBetter(nums, k))


main()
