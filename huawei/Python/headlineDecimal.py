while True:
    try:
        st = list(input())
        result = ''
        for i in range(len(st) - 1):
            if st[i].isdecimal() != st[i + 1].isdecimal():
                result += st[i]
                result += '*'
            else:
                result += st[i]
        result += st[-1]
        if st[0].isdecimal():
            result = '*' + result
        if st[-1].isdecimal():
            result += '*'
        print(result)
    except:
        break
            
            