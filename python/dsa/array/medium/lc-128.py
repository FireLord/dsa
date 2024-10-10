# optimal
def longestConsOpt(nums):
    n = len(nums)
    maxCtr = 0
    st = set()

    for i in range(n):
        st.add(nums[i])
    
    for i in st:
        if i - 1 not in st:
            currentCtr = 1
            x = i
            while x + 1 in st:
                x += 1
                currentCtr += 1
            maxCtr = max(maxCtr, currentCtr)
    
    return maxCtr


# better
def longestConsBetter(nums):
    n = len(nums)
    lastSmaller = float("-inf")
    maxCtr = 0
    currentCtr = 0
    nums.sort()

    for i in range(n):
        if nums[i] - 1 == lastSmaller:
            currentCtr += 1
            lastSmaller = nums[i]
        elif nums[i] != lastSmaller:
            currentCtr = 1
            lastSmaller = nums[i]

        maxCtr = max(maxCtr, currentCtr)

    return maxCtr


# brute
def longestCons(nums):
    n = len(nums)
    longest = 0

    for i in range(n):
        x = nums[i]
        cnt = 1
        while linearSearch(nums, x + 1) == True:
            x += 1
            cnt += 1

        longest = max(longest, cnt)

    return longest


def linearSearch(nums, k):
    for i in range(len(nums)):
        if nums[i] == k:
            return True

    return False


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    print(longestConsOpt(nums))


main()
