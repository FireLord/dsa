def moveZeroRightOpt():
    nums = [1, 2, 0, 0, 3, 0, 6, 7, 0, 8]
    n = len(nums)
    j = -1
    for i in range(n):
        if nums[i] == 0:
            j = i
            break

    for i in range(j + 1, n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    print(nums)


def moveZeroRight():
    x = [1, 2, 0, 0, 3, 0, 6, 7, 0, 8]
    zeroCount = x.count(0)

    # Create a new list without zeros
    y = []
    for i in range(len(x)):
        if x[i] != 0:
            y.append(x[i])

    # Append the zeros at the end
    for i in range(zeroCount):
        y.append(0)

    print(y)


def main():
    moveZeroRightOpt()


main()
