def pop(bot):
    if bot < 2:
        return 0
    elif bot == 2:
        return 1
    else:
        return bot // 3 + pop(bot // 3 + bot % 3)
    
while True:
    try:
        bottles = int(input())
        if bottles == 0:#为什么有时候通过这个无法正常退出循环
            break
        print(pop(bottles))
    except:
        break