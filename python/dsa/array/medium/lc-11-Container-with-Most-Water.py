def maxAreaOpti(height):
    size = len(height)
    l = 0
    r = size - 1
    maxArea = -1
    while (l<r):
        area = (r-l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return maxArea

def maxAreaBrute(height):
    size = len(height)
    maxArea = -1
    for i in range(size):
        for j in range(i+1, size):
            minHeight = min(height[i], height[j])
            maxArea = max(maxArea, minHeight*(j-i))
    return maxArea


def main():
    nums = [int(x) for x in input().split(",")]
    print(maxAreaBrute(nums))
    print(maxAreaOpti(nums))

main()