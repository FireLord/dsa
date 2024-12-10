def rotateArrayD(nums, k):
    # Get the length of the array
    n = len(nums)
    
    # Ensure k is within the bounds of the array length
    k = k % n
    
    # Slice the array into two parts and concatenate them in reversed order
    # nums[-k:] gives the last k elements of the array
    # nums[:-k] gives the elements from the start up to but not including the last k elements
    nums[:] = nums[-k:] + nums[:-k]
    
    # Print the rotated array
    print(nums)

def rotateArray1(nums):
    n = len(nums)
    last = nums[n - 1]
    for i in range(1, n):
        nums[n - i] = nums[n - (i + 1)]

    nums[0] = last
    print(nums)


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    # rotateArray1(nums)
    rotateArrayD(nums,n)

main()
