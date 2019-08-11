while True:
    try:
        line1 = input().split()
        line2 = input().split()
        m = int(line1[0])
        n = int(line1[1])
        data = []
        for i in line2:
            data.append(int(i))
        data.sort()
        for i in range(n):
            if i == n - 1:
                print(data[i])
            else:
                print(data[i], end = ' ')
    except:
        break