def floor(nums, k):
    n = len(nums)
    ans = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= k:
            ans = nums[mid]
            low = mid + 1 # look for smaller index on the right
        else:
            high = mid - 1 # look on the left
    return ans
            
        
def ceil(nums, k):
    n = len(nums)
    ans = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= k:
            ans = nums[mid]
            high = mid - 1 # look for smaller index on the left
        else:
            low = mid + 1 # look on the right
    return ans

def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(floor(nums, k))
    print(ceil(nums, k))

main()