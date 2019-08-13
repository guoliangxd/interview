import math
while True:
    try:
        rIndex = []
        rValue = []
        m, n = input().split()
        m = int(m)
        n = int(n)
        for i in range(m):
            k, v = input().split()
            k = int(k)
            v = int(v)
            if i != 0 and rIndex[i - 1] == k:
                continue
            else:
                rIndex.append(k)
                rValue.append(v)

        for i in range(len(rIndex) - 1):
            key = rIndex[i]
            nKey = rIndex[i + 1]
            print(key, end = ' ')
            print(rValue[i])
            if nKey == key + 1 or nKey < key:
                continue
            else:
                for j in range(1, nKey - key):
                    result = rValue[i] + math.trunc((rValue[i + 1] - rValue[i])/(nKey - key))*j
                    print(key + j, end = ' ')
                    print(result)
        print(rIndex[-1], end = ' ')
        print(rValue[-1])
    except:
        break
