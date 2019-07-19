def myRound(rawNum):
    if rawNum.find('.') == -1:
        return rawNum
    else:
        subStr = rawNum.split('.')
        result = int(subStr[0])
        if int(subStr[1][0]) >= 5:
            return result + 1
        else:
            return result

print(myRound(input()))