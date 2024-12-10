def frequencyCount(arr, N, P):
    freqDict = {i: 0 for i in range(1, N+1)}

    for i in arr:
        if i in freqDict:
            freqDict[i] += 1

    for i in range(N):
        arr[i] = freqDict[i+1]

def main():
    n = int(input())
    p = int(input())
    arr = [int(x) for x in input().split()]
    frequencyCount(arr, n, p)

main()