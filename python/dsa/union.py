def unionOptimal(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    union = []
    i = 0
    j = 0

    # Traverse both arrays
    while i < n and j < m:
        # If current element of arr1 is smaller or equal to current element of arr2
        if arr1[i] <= arr2[j]:
            # If union is empty or last element is not same as current element of arr1
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            # If union is empty or last element is not same as current element of arr2
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    # Store remaining elements of arr1
    while i < n:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Store remaining elements of arr2
    while j < m:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)


def union(arr1, arr2):
    seen = set()
    union = []
    for num in arr1:
        seen.add(num)

    for num in arr2:
        seen.add(num)

    for num in seen:
        union.append(num)

    union.sort()
    return union


def main():
    n = int(input())
    arr1 = [-7, 8]
    arr2 = [-8, -8, -3]
    print(unionOptimal(arr1, arr2))


main()
