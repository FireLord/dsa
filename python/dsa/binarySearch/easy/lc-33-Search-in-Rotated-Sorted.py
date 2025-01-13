def searchBinary(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid # the mid is the answer we are looking for which will be moving
        
        # check if left side is sorted from mid pivot
        if nums[low] <= nums[mid]:
            # check if target lies in left side
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1 # eliminate left half
            else:
                low = mid + 1 # eliminate right half
        # check if right side is sorted from mid pivot
        else:
            # check if target lies in right side
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1 


def main():
    k = int(input())
    nums = [int(x) for x in input().split(",")]
    print(searchBinary(nums, k))

main()
