def factor(x):
    if x == 1:
        return 1
    else:
        return (x * factor(x-1))

print(factor(3))