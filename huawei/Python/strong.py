while True:
    try:
        pw = input()
        score = 0
        upper = 0
        lower = 0
        decimal = 0
        symbol = 0
        
        for char in pw:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdecimal():
                decimal += 1
            else:
                symbol += 1
        
        if len(pw) <= 4:
            score += 5
        elif len(pw) <= 7:
            score += 10
        else:
            score += 25
            
        if upper + lower == 0:
            score += 0
        elif upper == 0 or lower == 0:
            score += 10
        else:
            score += 20
            
        if decimal == 0:
            score += 0
        elif decimal == 1:
            score += 10
        else:
            score += 20
            
        if symbol == 0:
            score += 0
        elif symbol == 1:
            score += 10
        else:
            score += 25
            
        if upper != 0 and lower != 0 and decimal != 0 and symbol != 0:
            score += 5
        elif (upper + lower != 0) and decimal != 0 and symbol != 0:
            score += 3
        elif (upper + lower != 0) and decimal != 0:
            score += 2
            
        if score >= 90:
            print("VERY_SECURE")
        elif score >= 80:
            print("SECURE")
        elif score >= 70:
            print("VERY_STRONG")
        elif score >= 60:
            print("STRONG")
        elif score >= 50:
            print("AVERAGE")
        elif score >= 25:
            print("WEAK")
        else:
            print("VERY_WEAK")
    except:
        break