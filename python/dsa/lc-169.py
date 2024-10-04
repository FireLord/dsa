# brute force
def majorityElement(nums):
    n = len(nums)
    countHash = {}
    for i in range(n):
        countHash[nums[i]] = countHash.get(nums[i], 0) + 1
    
    for (key, value) in countHash.items():
        if value > n//2:
            return key

    return -1


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(majorityElement(nums))

main()