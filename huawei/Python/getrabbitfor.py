#计算斐波那契数列-循环版
def getRabbit(mon):
    m1 = 1
    m2 = 1
    if mon <= 2:
        return 1
    else:
        for i in range(mon - 2):
            temp = m2
            m2 = m1 + m2
            m1 = temp
        return m2

while True:
    try:
        print(getRabbit(int(input())))
    except:
        break
