while True:
    try:
        st = input()
        if len(st) == 0:
            break
        count = {}
        for i in range(len(st)):
            if st[i] in count.keys():
                count[st[i]] += 1
            else:
                count[st[i]] = 1
        hasOne = False
        for i in range(len(st)):
            if count[st[i]] == 1:
                print(st[i])
                hasOne = True
                break
        if not hasOne:
            print(-1)
           
    except:
        break
        