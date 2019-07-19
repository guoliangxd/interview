dict = {}
num = int(input())
for i in range(num):
    keyValue = []
    keyValue.append(input())
    keyValue.append(input())
    if keyValue[0] in dict:
        dict[keyValue[0]] + int(keyValue[1])
    else:
        dict[keyValue[0]] = int(keyValue[1])
for key, value in dict:
    print(key, end = ' ')
    print(value)
#TODO:FixBug
