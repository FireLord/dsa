def countInversionsBetter(nums):
    # TC - n2
    # SC - 1
    n = len(nums)
    ctr = 0   
    return ctr

def countInversionsBrute(nums):
    # TC - n2
    # SC - 1
    n = len(nums)
    ctr = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                ctr += 1

    return ctr


def main():
    nums = [int(x) for x in input().split(",")]
    print(countInversionsBrute(nums))

main()
