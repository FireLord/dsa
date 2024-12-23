def subarrayXorOptimal(nums, k):
    n = len(nums)
    xr = 0
    hash = {}
    hash[xr] = 1
    count = 0
    for i in range(n):
        xr ^= nums[i]
        x = xr ^ k
        count += hash.get(x, 0)
        hash[xr] = hash.get(xr, 0) + 1

    return count


# important notice
def subarrayXorBetter(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        xorCount = 0
        for j in range(i, n):
            xorCount ^= nums[j]

            if xorCount == k:
                count += 1

    return count


def subarrayXorBrute(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            xorCount = 0
            for l in range(i, j + 1):
                xorCount ^= nums[l]
            if xorCount == k:
                count += 1

    return count


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(subarrayXorBrute(nums, n))
    print(subarrayXorBetter(nums, n))
    print(subarrayXorOptimal(nums, n))


main()
