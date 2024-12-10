def intersectionSorted():
    a = [1, 2, 2, 3, 3, 4, 5, 6]
    b = [2, 3, 3, 5, 6, 6, 7]
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    c = []

    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            c.append(a[i])
            i += 1
            j += 1

    print(c)

intersectionSorted()