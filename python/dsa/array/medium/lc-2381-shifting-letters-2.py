def shiftLetter2Opti(s, shifts):
    n = len(s)
    net_shifts = [0] * (n + 1)  # Use a difference array for range updates
    
    # Process each shift to update net_shifts
    for start, end, direction in shifts:
        shift_value = 1 if direction == 1 else -1
        net_shifts[start] += shift_value
        net_shifts[end + 1] -= shift_value  # Mark end of the range

    # Calculate cumulative shifts
    cumulative_shift = 0
    result = []
    for i in range(n):
        cumulative_shift += net_shifts[i]  # Apply cumulative effect
        shift = (ord(s[i]) - ord('a') + cumulative_shift) % 26
        result.append(chr(shift + ord('a')))  # Convert back to character

    return "".join(result)


def shiftLetter2Brute(s, shifts):
    result = list(s)
    for start, end, direction in shifts:
        for i in range(start, end + 1):
            if direction == 0:
                result[i] = chr((ord(result[i]) - ord('a') - 1) % 26 + ord('a'))
            else:
                result[i] = chr((ord(result[i]) - ord('a') + 1) % 26 + ord('a'))
    return "".join(result)


def main():
    s = "abc"
    shifts = [[0,1,0],[1,2,1],[0,2,1]]
    print(shiftLetter2Brute(s, shifts))


main()
