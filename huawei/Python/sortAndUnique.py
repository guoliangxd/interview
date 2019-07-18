# 对1000以内正整数排顺，去重
while True:
    try:
        num = int(input())
        inputList = []
        for i in range(num):
            inputList.append(int(input()))
        inputList.sort()
        lastNum = 0
        for i in range(num):
            if inputList[i] == lastNum:
                continue
            else:
                lastNum = inputList[i]
                print(inputList[i])
    except:
        break