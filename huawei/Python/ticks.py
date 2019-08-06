while True:
    try:
        n = int(input())
        can = input().split()
        m = int(input())
        ticks = input().split()
        
        result = {}
        for char in can:
            result[char] = 0
        
        invalid = 0
        
        for tick in ticks:
            if tick in result:
                result[tick] += 1
            else:
                invalid += 1
        
        for char in can:
            print(char + ' : ' + str(result[char]))
        print('Invalid : ' + str(invalid))
    except:
        break