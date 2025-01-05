def countVowelOptimized(words, queries):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    prefix = [0] * (len(words) + 1)

    for i, word in enumerate(words):
        if word[0] in vowels and word[-1] in vowels:
            prefix[i + 1] = prefix[i] + 1
        else:
            prefix[i + 1] = prefix[i]
    
    result = []
    for li, ri in queries:
        result.append(prefix[ri + 1] - prefix[li])
    
    return result

def isVowel(ch):
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        return True
    else:
        return False
    
def countVowelBrute(words, queries):
    result = []
    for item in queries:
        count = 0
        for i in range(item[0], item[1]+1):
            if isVowel(words[i][0]) and isVowel(words[i][-1]):
                count += 1
        result.append(count)
        
    return result
    
def main():
    words = ["bzmxvzjxfddcuznspdcbwiojiqf","mwguoaskvramwgiweogzulcinycosovozppl","uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs","uivcdsboxnraqpokjzaayedf","yalc","bbhlbmpskgxmxosft","vigplemkoni","krdrlctodtmprpxwditvcps","gqjwokkskrb","bslxxpabivbvzkozzvdaykaatzrpe","qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi","siqbezhkohmgbenbkikcxmvz","ddmaireeouzcvffkcohxus","kjzguljbwsxlrd","gqzuqcljvcpmoqlnrxvzqwoyas","vadguvpsubcwbfbaviedr","nxnorutztxfnpvmukpwuraen","imgvujjeygsiymdxp","rdzkpk","cuap","qcojjumwp","pyqzshwykhtyzdwzakjejqyxbganow","cvxuskhcloxykcu","ul","axzscbjajazvbxffrydajapweci"]
    queries = [[4, 4],[6, 17],[10, 17],[9, 18],[17, 22],[5, 23],[2, 5],[17, 21],[5, 17],[4, 8],[7, 17],[16, 19],[7, 12],[9, 20],[13, 23],[1, 5],[19, 19]]
    print(countVowelBrute(words, queries))

main()