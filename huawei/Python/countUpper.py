while True:
    try:
        st = input()
        n = 0
        for i in st:
            if i >= 'A' and i <= 'Z':
                n += 1
        print(n)
    except:
        break