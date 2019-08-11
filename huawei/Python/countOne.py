while True:
    try:
        num = int(input())
        binStr = bin(num)
        n = 0
        for char in binStr:
            if char == '1':
                n += 1
        print(n)
    except:
        break
        