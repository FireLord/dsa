def binarySearchIterative(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(binarySearchIterative(nums, k))

main()