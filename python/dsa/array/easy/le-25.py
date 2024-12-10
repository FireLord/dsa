def rmDuplicatesOptimal(nums):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]
    print(k+1)
    print(nums)

def removeDuplicates(nums):
    n = len(nums)
    seen = set()
    for i in range(n):
        seen.add(nums[i])
    
    seenSize = len(seen)
    count = 0
    for i in seen:
        nums[count] = i
        count += 1
    
    print(seenSize)
    print(nums)



def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    rmDuplicatesOptimal(nums)

main()