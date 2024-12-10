def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    size = input()
    arr = input()
    num_list = [int(x) for x in arr.split()]
    result = containsDuplicate(num_list)
    print(result)

main()