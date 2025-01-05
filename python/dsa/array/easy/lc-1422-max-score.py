def maxScoreSplitBrute(s):
    n = len(s)
    nums = [int(x) for x in s]
    count = 0
    for i in range(n):
        countZero = nums[:i+1].count(0)
        countOne = nums[i+1:n].count(1)

        count = max(count, countZero + countOne)
    return count


def main():
    str = input()
    print(maxScoreSplitBrute(str))


main()
