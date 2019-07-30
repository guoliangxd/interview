while True:
    try:
        key = input().lower()
        data = input()
        mapList = {}
        index = 'a'
        for char in key:
            if char in mapList.values():
                continue
            else:
                mapList[index] = char
                index = chr(ord(index) + 1)
        for i in range(26):
            char = chr(ord('a') + i)
            if char in mapList.values():
                continue
            else:
                mapList[index] = char
                index = chr(ord(index) + 1)
                
        result = ''
        for char in data:
            if char.islower():
                result += mapList[char]
            else:
                result += mapList[char.lower].upper()
        print(result)
    except:
        break
            
        