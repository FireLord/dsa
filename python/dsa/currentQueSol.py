def fact(n):
    # ! tail recursion
    
    # base case
    if n==0:
        return
    
    # recursive relation
    return fact(n-1)

    # process
    print(n)
    
n=int(input("Enter a num:"))
print(fact(n))