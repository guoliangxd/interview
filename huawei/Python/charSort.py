#TODO:复习排序算法和对应的接口
while True:
    try:
        charSet = {}
        chars = input()
        str1 = ''
        for char in chars:
            if char.isalpha() or char.isdecimal or char.isspace():
                if char in charSet:
                    charSet[char] += 1
                else:
                    charSet[char] = 1
                    
        d2 = sorted(sorted(charSet.items(), key=lambda x: x[0]), key = lambda item:item[1], reverse = True)
        str1 = ''.join([k for (k, v) in d2])
        print(str1)

    except:
        break