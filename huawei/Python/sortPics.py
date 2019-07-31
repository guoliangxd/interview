#注意sorted也是python的内建函数
while True:
    try:
        pics = input()
        result = list(pics)
        result.sort()
        for char in result[ : -1]:
            print(char, end = '')
        print(result[-1])
    except:
        break