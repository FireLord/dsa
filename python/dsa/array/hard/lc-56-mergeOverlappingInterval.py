def mergeOverlapOptimal(nums):
    n = len(nums)
    nums.sort()
    result = []

    for i in range(n):
        if not result or nums[i][0] > result[-1][1]:
            result.append(nums[i])
        else:
            result[-1][1] = max(result[-1][1], nums[i][1])

    return result


def mergeOverlapBrute(nums):
    n = len(nums)
    nums.sort()
    result = []

    for i in range(n):
        start = nums[i][0]
        end = nums[i][1]
        if result and end <= result[-1][1]:
            continue
        for j in range(i+1, n):
            if nums[j][0] <= end:
                end = max(end, nums[j][1])
            else:
                break
        result.append([start, end])

    return result


def main():
    n = int(input())
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(mergeOverlapBrute(nums))
    print(mergeOverlapOptimal(nums))


main()
