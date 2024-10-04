# optimal for +ve zero positives
def longestSubArrayOpt(nums, k):
    n = len(nums)
    left = 0
    right = 0
    sumOfNum = nums[0]
    maxLen = 0
    
    # Iterate through the array with the right pointer
    while right < n:
        # Adjust the left pointer to maintain the sum <= k
        while left <= right and sumOfNum > k:
            sumOfNum -= nums[left]
            left += 1
        
        # Check if the current subarray sum equals k
        if sumOfNum == k:
            maxLen = max(maxLen, right - left + 1)
        
        # Move the right pointer to the next element
        right += 1
        if right < n:
            sumOfNum += nums[right]
    
    return maxLen

# optimal for -ve zero positives but better for +ve and zero
def longestSubArrayBetter(nums, k):
    n = len(nums)
    preSumMap = {}
    maxLen = 0
    sumOfNum = 0

    for i in range(n):
        sumOfNum += nums[i]
        if sumOfNum == k:
            maxLen = max(maxLen, i + 1)

        rem = sumOfNum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        
        if sumOfNum not in preSumMap:
            preSumMap[sumOfNum] = i

    return maxLen


# brute 2
def longestSubArray2(nums, k):
    n = len(nums)
    maxLen = 0
    for i in range(n):
        subArraySum = 0
        for j in range(i, n):
            subArraySum += nums[j]
            if subArraySum == k:
                maxLen = max(maxLen, j - i + 1)

    return maxLen


# brute 1
def longestSubArray(nums, k):
    n = len(nums)
    maxLen = 0
    for i in range(n):
        for j in range(i, n):
            subArraySum = 0
            for l in range(i, j + 1):
                subArraySum += nums[l]
            if subArraySum == k:
                maxLen = max(maxLen, j - i + 1)

    return maxLen


def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(longestSubArrayOpt(nums, k))


main()
