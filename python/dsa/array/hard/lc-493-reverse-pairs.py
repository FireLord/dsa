def reversePairBetter(nums):
    n = len(nums)
    ctr = 0

    return ctr

def reversePairBrute(nums):
    n = len(nums)
    ctr = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > 2 * nums[j]:
                ctr += 1

    return ctr


def main():
    nums = [int(x) for x in input().split(",")]
    print(reversePairBrute(nums))

main()
