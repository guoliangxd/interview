def toBinary(stri):
    num = int(stri)
    result = ''
    for i in range(8):
        result += str(num % 2)
        num = num // 2
    return result

def isValidMask(stri):
    subMask = stri.split('.')
    if len(subMask) != 4:
        return False
    else:
        toStr = toBinary(subMask[0]) + toBinary(subMask[1]) + toBinary(subMask[2]) + toBinary(subMask[3])
        change = 0
        for i in range(32 - 1):
            if toStr[i] != toStr[i + 1]:
                change += 1
        if change == 0: and toStr[0] == '0'
            return True
        elif change == 1:
            if toStr[0] == '1':
                return True
            else:
                return False
        else:
            return False

typeA = 0
typeB = 0
typeC = 0
typeD = 0
typeE = 0
valid = 0
priva = 0

while True:
    try:
        ip = input()
        if len(ip) == 0:
            break
        else:
            subIP = ip.split('~')
            if len(subIP) != 2:
                break
            else:
                if isValidMask(subIP[1]):
                    subAddress = subIP[0].split('.')
                    first = 0
                    second = 0
                    if len(subAddress[0]) == 0:
                        valid += 1
                        continue
                    else:
                        first = int(subAddress[0])
                    if len(subAddress[1]) == 0:
                        valid += 1
                        continue
                    else:
                        second = int(subAddress[1])
                    if first >= 1 and first <= 126:
                        typeA += 1
                    if first >= 128 and first <= 191:
                        typeB += 1
                    if first >= 192 and first <= 223:
                        typeC += 1
                    if first >= 224 and first <= 239:
                        typeD += 1
                    if first >= 240 and first <= 255:
                        typeE += 1
                    if first  == 10:
                        priva += 1
                    if first == 172 and (second >= 16 and second <= 31):
                        priva += 1
                    if first == 192 and second == 168:
                        priva += 1
                    if first == 127 or first < 1 or first > 255:
                        valid += 1
                else:
                    valid += 1
                    continue
    except:
        break

print(typeA, end = ' ')
print(typeB, end = ' ')
print(typeC, end = ' ')
print(typeD, end = ' ')
print(typeE, end = ' ')
print(valid, end = ' ')
print(priva)