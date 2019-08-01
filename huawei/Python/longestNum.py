import sys
for line in sys.stdin:
        st = line
        nums = []
        length = 0
        maxLen = 0
        for i in range(len(st)):
            if st[i].isdecimal():
                length += 1
            else:
                if length != 0:
                    if length >= maxLen:
                        maxLen = length
                        nums.append(st[i - length : i])
                    length = 0
        if maxLen == 0:
            print('', end = '')
            continue
        if st[-1].isdecimal():
            if length >= maxLen:
                maxLen = length
                nums.append(st[len(st) - length : ])
        result = ''
        for num in nums:
            if len(num) == maxLen:
                result  += num
        print(result + ',' + str(maxLen))
                
                    
                     
            
            