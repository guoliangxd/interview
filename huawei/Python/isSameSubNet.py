def toBinaryList(ipOrMask):
    subStr = ipOrMask.split('.')
    result = []
    for sub in subStr:
        num = int(sub)
        temp = []
        for i in range(8):
            temp.insert(0, num % 2)
            num = num // 2
        result += temp
        if len(result) != 32:
            for i in range(32 - len(result)):
                result.append(0)
    return result

def isSameSubNet(mask, ip1, ip2):
        for i in range(32):
            ip1[i] = ip1[i] * mask[i]
            ip2[i] = ip2[i] * mask[i]
        if ip1 == ip2:
            return True
        else:
            return False
            
def isValidMask(mask):
        subMask = mask.split('.')
        maskList = []
        for subStr in subMask:
            num = int(subStr)
            if num >= 0 and num <= 255:
                temp = []
                for i in range(8):
                    temp.insert(0, num % 2)
                    num = num // 2
                maskList += temp
            else:
                print('value = ' + str(num))
                return False
        if len(maskList) < 32:
            for i in range(32 - len(maskList)):
                maskList.append(0)
        change = 0
        for i in range(31):
            if maskList[i] != maskList[i + 1]:
                change += 1
            else:
                continue
        if change == 0 or (change == 1 and maskList[0] == 1):
            return True
        else:
            print('change = ' + str(change))
            return False

    
def isValidIP(ip):
    try:
        subIP = ip.split('.')
        for i in range(4):
            num = int(subIP[i])
            if num >= 0 and num <= 255:
                continue
            else:
                return False
        return True
    except:
        return False

while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()
        if isValidMask(mask) and isValidIP(ip1) and isValidIP(ip2):
            if isSameSubNet(toBinaryList(mask), toBinaryList(ip1), toBinaryList(ip2)):
                print(0)
            else:
                print(2)
        else:
            print(1)
    except:
        break