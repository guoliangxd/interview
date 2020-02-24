while True:
    try:
        data = input()
        line = (len(data) + 7) // 8
        for i in range(line):
            begin = 8 * i
            end   = 8 * i + 8
            temp = data[begin : end]
            print(data[begin : end] + '0' * (8 - len(temp)))
    except:
        break