def maxProdSubArrayOpti(nums):
    n = len(nums)
    prefix = 1
    suffix = 1
    result = float("-inf")
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - i - 1]
        result = max(result, max(prefix, suffix))
    return result


def maxProdSubArrayBetter(nums):
    n = len(nums)
    result = -1
    for i in range(n):
        prod = nums[i]
        for j in range(i+1, n):
            prod *= nums[j]
            result = max(result, prod)

    return result

def maxProdSubArrayBrute(nums):
    n = len(nums)
    result = -1
    for i in range(n):
        for j in range(i+1, n):
            prod = 1
            for k in range(i, j+1):
                prod *= nums[k]
            result = max(result, prod)

    return result


def main():
    nums = [int(x) for x in input().split(",")]
    print(maxProdSubArrayBrute(nums))
    print(maxProdSubArrayBetter(nums))
    print(maxProdSubArrayOpti(nums))


main()