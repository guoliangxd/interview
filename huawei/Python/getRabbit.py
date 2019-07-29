#斐波那契数列-递归解法
def getRabbit(mon):
    if mon == 1 or mon == 2:
        return 1
    else:
        return getRabbit(mon - 1) + getRabbit(mon - 2)
    
while True:
    try:
        print(getRabbit(int(input())))
    except:
        break