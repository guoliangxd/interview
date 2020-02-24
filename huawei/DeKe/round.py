while True:
    try:
        data = input().split('.')
        if int(data[1][0]) >= 5:
           print(int(data[0]) + 1)
        else:
           print(data[0])
    except:
        break