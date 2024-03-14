def pattern(n):
    for i in range(1, 2*n):
        stars = i
        if i > n:
            stars = 2*n-i
        for j in range(stars):
            print('*', end="")
        print()
        
def main():
    n = int(input("Enter a number: "))
    pattern(n)

if __name__ == "__main__":
    main()