#注意审题
while True:
    try:
        data = []
        for i in range(2):
            input()
            ar = input().split()
            for j in range(len(ar)):
                num = int(ar[j])
                if num in data:
                    continue
                else:
                    data.append(num)
        data.sort()
        for i in range(len(data)):
            print(data[i], end = '')
        print()
    except:
        break