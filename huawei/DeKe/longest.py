def findLongestSub(rawStr):
    index = 0
    maxLen = 1
    curLen = 1
    if len(rawStr) <= 1:
        return rawStr
    for i in range(1, len(rawStr)):
        if rawStr[i - 1] == rawStr[i]:
            curLen += 1
        else:
            if curLen > maxLen:
                maxLen = curLen
                index = i - maxLen
            elif curLen == maxLen:
                if rawStr[index] > rawStr[i - 1]:
                    index = i - maxLen
            curLen = 1
    return rawStr[index : index + maxLen]

data = input()
print(findLongestSub(data))
