#这道题本身用例有问题，Python怎么处理精度都不行
while True:
    try:
        high = int(input())
        total = ''
        last = ''
        if high == 0:
            print(0)
            print(0)
        else:
            total += str(high * 2875)
            last += str(high * 3125)
            total = total[0 : -3] + '.' + total[-3 : ]
            if len(last) == 4:
                last = '00' + last
            elif len(last) == 5:
                last = '0' + last
            last = last[0 : -5] + '.' + last[-5 : ]
            print(total)
            print(last)
    except:
        break