def sortedRotated(arr):
    # Get the length of the array
    n = len(arr)
    
    # Initialize a counter to track the number of drop points
    dropPoint = 0
    
    # Iterate through the array
    for i in range(n):
        # Calculate the next index in a circular manner
        t = (i + 1) % n
        
        # Check if the current element is greater than the next element
        if arr[i] > arr[t]:
            # Increment the drop point counter
            dropPoint += 1

    # If there is more than one drop point, the array is not sorted and rotated
    if dropPoint > 1:
        return False

    # If there is at most one drop point, the array is sorted and rotated
    return True


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(sortedRotated(arr))


main()
