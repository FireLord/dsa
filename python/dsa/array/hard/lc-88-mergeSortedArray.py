def mergeSortedOptimal(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    left = n-1
    right = 0

    while left >= 0 and right < m:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break
    
    nums1.sort()
    nums2.sort()

    return (nums1, nums2)


def mergeSortedBetter(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    result = [0] * (n + m)
    left = 0
    right = 0
    index = 0

    while left < n and right < m:
        if nums1[left] <= nums2[right]:
            result[index] = nums1[left]
            left += 1
            index += 1
        else:
            result[index] = nums2[right]
            right += 1
            index += 1

    while left < n:
        result[index] = nums1[left]
        left += 1
        index += 1

    while right < m:
        result[index] = nums2[right]
        right += 1
        index += 1

    for i in range(n+m):
        if i < n:
            nums1[i] = result[i]
        else:
            nums2[i-n] = result[i]

    return result

def mergeSortedBrute(nums1, nums2):
    nums1 += nums2
    nums1.sort()

    return nums1


def main():
    n = int(input())
    nums1 = [int(x) for x in input().split(",")]
    nums2 = [int(x) for x in input().split(",")]
    print(mergeSortedBetter(nums1, nums2))
    print(mergeSortedOptimal(nums1, nums2))


main()
