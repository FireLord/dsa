def countNum(n):
    reverseNum = 0
    initVal = n
    MAX_INT = 2 ** 31 - 1

    if n < 0:
        n*=-1
    while(n > 0):
        if reverseNum > MAX_INT / 10 :
            return 0
        remainder = n%10
        n = n // 10
        reverseNum = (reverseNum*10) + remainder

    if initVal < 0:
        print(f"ReverseNum is: {reverseNum*-1}")
    else:
        print(f"ReverseNum is: {reverseNum}")

def palindrome(x):
    initVal = x
    reverseNum = 0
    
    if x < 0:
        print("false")
        
    while(x>0):
        remainder = x%10
        x = x // 10
        reverseNum = (reverseNum*10) + remainder
    
    if initVal == reverseNum:
        print("true")
    else:
        print("false")

def palindrome2(x):
    y=str(x)
    z=y[::-1]
    if y==z:
        return print("true")
    else:
        return print("false")
    
def armstrongNum(x):
    dupX=x
    initSum = 0
    countDigit = 0
    digitList = []

    while(x>0):
        reminder = x % 10
        x = x // 10
        digitList.append(reminder)
        countDigit += 1
    
    initSum = sum(digit ** countDigit for digit in digitList)

    if initSum==dupX:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

def sumDivisor(x):
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
    
def sumDivisorOptimal(x):
    numList = []
    squareRoot = int(x ** 0.5)
    for i in range(1, squareRoot+1):
        if x % i == 0:
            numList.append(i)
            if (x // i != i):
                numList.append(x//i)

    numList.sort()
    for item in numList:
        print(item)

def primeNum(x):
    countPrime = 0
    for i in range(1, x+1):
        if (x % i == 0):
            countPrime += 1
            
    if (countPrime == 2):
        print("Its a prime number")
    else:
        print("Its not a prime number")

def primeNumOptimal(x):
    countPrime = 0
    squareRoot = int(x ** 0.5)
    for i in range(1, squareRoot+1):
        if (x % i == 0):
            countPrime += 1
            if (x // i != i):
                countPrime += 1
    
    if (countPrime == 2):
        print("Its a prime number")
    else:
        print("Its not a prime number")

def gcd(num1, num2):
    minNum = min(num1, num2)
    gcd = 0
    for i in range(1, minNum + 1):
        if ((num1 % i == 0) and (num2 % i ==0)):
            gcd = i
    
    print(f"GCD: {gcd}")

def gcdOptimal(num1, num2):
    while(num1 > 0 and num2 > 0):
        if (num1 > num2):
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    
    if (num1 == 0):
        print(f"GCD: {num2}")
    else:
        print(f"GCD: {num1}")

def main():
    n = int(input())
    m = int(input())
    # countNum(n)
    # palindrome(n) f
    # palindrome2(n)
    # armstrongNum(n)
    # sumDivisor(n)
    # sumDivisorOptimal(n)
    # primeNum(n)
    # primeNumOptimal(n)
    # gcd(n,m)
    gcdOptimal(n,m)

main()