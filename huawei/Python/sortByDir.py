num = int(input())
strList = []
for i in range(num):
    strList.append(input())
strList.sort()
for i in range(num):
    print(strList[i])