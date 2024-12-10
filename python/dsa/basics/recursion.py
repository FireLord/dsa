def nameRec(start, times):
    if (start > times):
        return
    
    print("aman")
    nameRec(start+1, times)

    
def sumOfNum(num,sum):
    if (num < 1):
        print(sum)
        return
    
    sumOfNum(num-1, sum+num)
    
def sumOfNumFunctional(num):
    if (num < 1):
        return 0
    
    return num + sumOfNumFunctional(num-1)

def factorialRec(num):
    if (num < 1):
        return 1
    
    return num * factorialRec(num-1)

def reverseArrayRec(start, end, arr):
    if (start >= end//2):
        return
    
    # swap
    arr[start], arr[end-start-1] = arr[end-start-1], arr[start]

    reverseArrayRec(start + 1, end, arr)

def palindromeRec(start, size, s):
    if (start >= size // 2):
        return True
    
    if (s[start] != (size - start - 1)):
        return False

    ## buggy    
    return palindromeRec(start + 1, size, s)

def multiRecCalFib(n):
    if (n <= 1):
       return n
    
    last = multiRecCalFib(n-1)
    sLast = multiRecCalFib(n-2)

    return last + sLast
    
def main():
    x = int(input())
    y = int(input())
    # nameRec(x, y)
    # sumOfNum(x,0)
    # print(sumOfNumFunctional(x))
    # print(factorialRec(x))
    # arr = [1,2,3,4,5,6]
    # reverseArrayRec(0, len(arr), arr)
    # print(arr)
    # s = "madam"
    # u = palindromeRec(0, len(s), s)
    # print(u)
    print(multiRecCalFib(x))

main()