# optimal - dutch national flag algo
def sortColorsOpt(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
            
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# better
def sortColors(nums):
    n = len(nums)
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(n):
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        elif nums[i] == 2:
            count2 += 1

    for i in range(count0):
        nums[i] = 0

    for i in range(count0, count0 + count1):
        nums[i] = 1

    for i in range(count0 + count1, count0 + count1 + count2):
        nums[i] = 2


def main():
    n = int(input())
    nums = [int(x) for x in input().split(",")]
    sortColors(nums)
    print(nums)


main()
