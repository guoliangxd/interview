while True:
    try:
        decimal = int(input())
        byte = bin(decimal)[2 : ]
        bits = byte.split('0')
        Max = 0
        for sub in bits:
            if len(sub) > Max:
                Max = len(sub)
        print(Max)
    except:
        break