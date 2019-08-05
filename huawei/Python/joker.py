while True:
    try:
        poker = input().split('-')
    
        dec1 = []
        dec2 = []
        for char in poker[0].split():
            if char == 'J':
                dec1.append(11)
            elif char == 'Q':
                dec1.append(12)
            elif char == 'K':
                dec1.append(13)
            elif char == 'A':
                dec1.append(14)
            elif char == '2':
                dec1.append(15)
            elif char == 'joker':
                dec1.append(16)
            elif char == 'JOKER':
                dec1.append(17)
            elif char.isdecimal():
                dec1.append(int(char))
            
        for char in poker[1].split():
            if char == 'J':
                dec2.append(11)
            elif char == 'Q':
                dec2.append(12)
            elif char == 'K':
                dec2.append(13)
            elif char == 'A':
                dec2.append(14)
            elif char == '2':
                dec2.append(15)
            elif char == 'joker':
                dec2.append(16)
            elif char == 'JOKER':
                dec2.append(17)
            elif char.isdecimal():
                dec2.append(int(char))
    
        if poker[0] == 'joker JOKER':
            print(poker[0])
        elif poker[1] == 'joker JOKER':
            print(poker[1])
        elif len(dec1) == 4:
            if len(dec2) != 4:
                print(poker[0])
            else:
                if dec1[0] > dec2[0]:
                    print(poker[0])
                else:
                    print(poker[1])
        elif len(dec2) == 4:
            print(poker[1])
        else:
            if len(dec1) != len(dec2):
                print("ERROR")
            elif dec1[0] > dec2[0]:
                print(poker[0])
            else:
                print(poker[1])
            
    except:
        break