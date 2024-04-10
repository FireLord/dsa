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
    return

def main():
    n = int(input(""))
    # countNum(n)
    # palindrome(n)
    # palindrome2(n)
    armstrongNum(n)


main()