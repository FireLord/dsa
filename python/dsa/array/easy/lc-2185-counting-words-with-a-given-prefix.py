def countingWordBrute(words, pref):
    count = 0
    prefSize = len(pref)
    for word in words:
        if pref in word[:prefSize]:
            count += 1
    return count

def main():
    pref = input()
    words = [x for x in input().split(",")]
    print(countingWordBrute(words, pref))

main()