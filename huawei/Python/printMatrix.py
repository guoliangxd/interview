while True:
    try:
        data = []
        line = int(input())
        for i in range(line):
            col = line - i
            row = []
            for j in range(col):
                if j == 0:
                    data.append(row)
                    if i == 0:
                        row.append(1)
                    else:
                        row.append(data[i - 1][0] + i)
                else:
                    row.append(row[j - 1] + j + i + 1)
        for row in data:
            for i in row[:-1]:
                print(i, end=" ")
            print(row[-1])
    except:
        break
