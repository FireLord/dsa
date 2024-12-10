def stairCase(n):
    # base case 1
    if n<0:
        return 0 # ground me koi stair nhi hota
    if n==0:
        return 1 # wahi uspar kudega
    # RR
    return stairCase(n-1)+stairCase(n-2)

print(stairCase(2))