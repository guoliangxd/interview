while True:
    try:
        _str = input()
        alpha = 0
        space = 0
        digit = 0
        other = 0
        for char in _str:
            if char.isalpha():
                alpha += 1
            elif char.isspace():
                space += 1
            elif char.isdecimal():
                digit += 1
            else:
                other += 1
        print(alpha)
        print(space)
        print(digit)
        print(other)
    except:
        break