def getInd(n):
    if n <= 2:
        return -1
    elif n % 2 == 1:
        return 2
    elif n % 4 == 0:
        return 3
    else:
        return 4
def getIndex(n):
    if n <= 2:
        return -1
    data = []
    for i in range(n):
        temp = []
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i: # 每行第一个和最后一个元素为1
                temp.append(1)
            else:
                left  = j -2
                top   = j -1
                right = j
                last = i - 1
                now = 0
                if j - 2 >= 0:
                    now += data[last][left]
                now += data[last][top]
                if j <= 2 * i - 2:
                    now += data[last][right]
                temp.append(now)
        data.append(temp)
    for i in range(len(data[-1])):
        if data[-1][i] % 2 == 0:
            return i + 1
        
while True:
    try:
        line = int(input())
        print(getInd(line))
    except:
        break
                
            
            
    