def countDaysBrute(days, meetings):
    totalDays = [int(x) for x in range(1,days+1)]
    for item in meetings:
        for i in range(item[0], item[1]+1):
            if totalDays[i] != None:
                totalDays.remove(i)
    return len(totalDays)

def main():
    n = 5
    nums = [[2,4],[1,3]]
    print(countDaysBrute(n, nums))

main()