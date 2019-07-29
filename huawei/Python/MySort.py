def mySort(rawStr):
    result = ''
    alpha = []
    for char in rawStr:
        if char.isalpha():
            if len(alpha) == 0:
                alpha.append(char)
                continue
            for i in range(len(alpha)):
                if char.lower() >= alpha[i].lower():
                    if i == len(alpha) - 1:
                        alpha.append(char)
                        break
                    else:
                        continue
                else:
                    alpha.insert(i, char)
                    break
    index = 0
    for i in range(len(rawStr)):
        if rawStr[i].isalpha():
            result += alpha[index]
            index += 1
        else:
            result += rawStr[i]
    return result
    
while True:
    try:
        rawStr = input()
        print(mySort(rawStr))
    except:
        break