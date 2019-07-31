while True:
    try:
        n = int(input())
        sume = 0
        countA = 0
        countB = 0
        for i in range(n):
            num = int(input())
            if num > 0:
                sume += num
                countA += 1
            elif num < 0:
                countB += 1
    
        print(countB, end = " ")
        avg = sume * 10 // countA
        avg = str(avg)
        if avg[-1] == '0':
            print(avg[ : -1])
        else:
            print(avg[ : -1] + '.' + avg[-1])
    except:
        continue
    