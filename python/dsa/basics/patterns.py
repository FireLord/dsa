def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()


def pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print()


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print()


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(f"{i} ", end="")
        print()


def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()


def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(f"{j+1} ", end="")
        print()


def pattern7(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        for j in range(n - i - 1):
            print(" ", end="")
        print()


def pattern8(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        for j in range(n - i):
            print(" ", end="")
        print()


def pattern9(n):
    pattern7(n)
    pattern8(n)


def pattern10(n):
    for i in range(1, 2 * n):
        stars = i
        if i > n:
            stars = 2 * n - i

        for j in range(1, stars + 1):
            print("*", end="")
        print()


def pattern11(n):
    start = 0
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(f"{start} ", end="")
            start = 1 - start  # to flip the 0 or 1
        print()


def pattern12(n):
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        # numbers
        for j in range(1, i + 1):
            print(f"{j} ", end="")

        # spaces
        for j in range(1, space + 1):
            print("  ", end="")

        # numbers
        for j in range(i, 0, -1):
            print(f"{j} ", end="")

        print()
        space -= 2


def pattern13(n):
    count = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(f"{count} ", end="")
            count += 1
        print()


def pattern14(n):
    count = 65
    for i in range(1, n + 1):
        for _ in range(i):
            print(f"{chr(count)} ", end="")
            count += 1
        count = 65
        print()


def pattern15(n):
    count = 65
    for i in range(n, 0, -1):
        for _ in range(i):
            print(f"{chr(count)} ", end="")
            count += 1
        count = 65
        print()


def pattern16(n):
    count = 65
    for i in range(n):
        for _ in range(i + 1):
            print(f"{chr(count)} ", end="")

        count += 1
        print()


def pattern17(n):
    for i in range(n):
        # spaces
        for j in range(n - i - 1):
            print("-", end="")

        # chars
        char = ord("A")
        breakpoint = (2 * i + 1) // 2
        for j in range(2 * i + 1):
            print(f"{chr(char)} ", end="")
            if j < breakpoint:
                char += 1
            else:
                char -= 1

        # spaces
        for j in range(n - i - 1):
            print("-", end="")

        print()


def pattern18(n):
    for i in range(n):
        for ch in range(ord("E") - i, ord("F")):
            print(f"{chr(ch)} ", end="")
        print()


def pattern19(n):
    initSpace = 0
    for i in range(n):
        # stars
        for _ in range(n - i):
            print("*", end=" ")

        # spaces
        for _ in range(initSpace):
            print(" ", end=" ")

        # stars
        for _ in range(n - i):
            print("*", end=" ")

        initSpace += 2
        print()

    initSpace = 8
    for i in range(n):
        # stars
        for _ in range(i + 1):
            print("*", end=" ")

        # spaces
        for _ in range(initSpace):
            print(" ", end=" ")

        # stars
        for _ in range(i + 1):
            print("*", end=" ")

        initSpace -= 2
        print()


def pattern20(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        stars = i
        if i > n:
            stars = 2 * n - i

        # stars
        for _ in range(1, stars + 1):
            print("*", end=" ")

        # spaces
        for _ in range(spaces):
            print(" ", end=" ")

        # stars
        for _ in range(1, stars + 1):
            print("*", end=" ")

        print()
        if i < n:
            spaces -= 2
        else:
            spaces += 2


def pattern21(n):
    for i in range(n):
        for j in range(n):
            if (
                i == 0 or j == 0 or i == n - 1 or j == n - 1
            ):  # boundary ka sochna hai bus
                print("*", end="")
            else:
                print(" ", end="")
        print()


def pattern22(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            # here we have to find the distance of the digit from the boundaries then min of it
            top = i
            left = j
            right = (2 * n - 2) - j
            down = (2 * n - 2) - i
            print(n - min(min((top, down)), min(left, right)), end="")
        print()


def main():
    n = int(input(""))
    # pattern1(n)
    # pattern2(n)
    # pattern3(n)
    # pattern4(n)
    # pattern5(n)
    # pattern6(n)
    # pattern7(n) important!
    # pattern8(n)
    # pattern9(n)
    # pattern10(n)
    # pattern11(n)
    # pattern12(n)
    # pattern13(n)
    # pattern14(n)
    # pattern15(n)
    # pattern16(n)
    # pattern17(n) important!
    # pattern18(n) important!
    # pattern19(n) important!
    # pattern20(n) important!
    # pattern21(n) important!
    pattern22(n)


if __name__ == "__main__":
    main()
