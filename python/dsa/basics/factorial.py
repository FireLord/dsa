def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    print(total)

def factorialRecursive(n):
    if n == 1:
        return n
    else:
        return n*factorialRecursive(n-1)


def main():
    x = int(input())
    factorial(x)
    
    # if x < 0:
    #     print("Sorry, factorial does not exist for negative numbers")
    # elif x == 0:
    #     print(1)
    # else:
    #     print(factorialRecursive(x))
    
    # fibonacci(x)
    
    # if x <= 0:
    #     print("Please enter a positive integer")
    # else:
    #     print("Fibonacci sequence:")
    # for i in range(x):
    #     print(fibRec(i))

    # array = [3, 4, 5, 6, 7, 8, 9]
    # x = 4
    # result = binarySearch(array,x)
    # if result != -1:
    #     print("Element is present at index " + str(result))
    # else:
    #     print("Not found")


main()