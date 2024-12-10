def singleNumXor(nums):
    n = len(nums)
    xor1 = 0
    for num in nums:
        xor1 ^= num

    return xor1

def singleNum(nums):
    n = len(nums)
    count = 0
    freq = {}

    for i in range(n):
        freq[nums[i]] = freq.get(nums[i], 0) + 1

    for (key, value) in freq.items():
        if value == 1:
            count = key
            
    return count


def main():
    nums = [int(x) for x in input().split()]
    # print(singleNum(nums))
    print(singleNumXor(nums))

main()