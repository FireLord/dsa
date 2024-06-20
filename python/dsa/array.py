def moveZeroRight():
    x = [1, 2, 0, 0, 3, 0, 6, 7, 0, 8]
    zeroCount = x.count(0)

    # Create a new list without zeros
    y = []
    for i in range(len(x)):
        if (x[i] != 0):
            y.append(x[i])

    # Append the zeros at the end
    for i in range(zeroCount):
        y.append(0)

    print(y)

def main():
    moveZeroRight()

main()