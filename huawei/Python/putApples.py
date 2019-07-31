#用迭代进行求解
def getFuns(m, n):
    if m == 0 or n == 1:
        return 1
    elif n > m:
        return getFuns(m, m)
    else:
        return getFuns(m, n - 1) + getFuns(m - n, n) #有空盘子，没有空盘子
while True:
    try:
        data = input().split()
        m = int(data[0])
        n = int(data[1])
        print(getFuns(m, n))
    except:
        break
        