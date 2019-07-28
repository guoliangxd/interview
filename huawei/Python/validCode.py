ok = "OK"
ng = "NG"
def lenValid(str_):
    if len(str_) <= 8:
        return False
    else:
        return True
    
def charValid(str_):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for char in str_:
        if char >= 'a' and char <= 'z':
            num1 = 1
        elif char >= 'A' and char <= 'Z':
            num2 = 1
        elif char >= '0' and char <= '9':
            num3 = 1
        else:
            num4 = 1
    if num1 + num2 + num3 + num4 >= 3:
        return True
    else:
        return False
    
def repeatValid(str_):
    for i in range(len(str_) - 3):
        if str_[i : i + 3] in str_[i + 1 :]:
            return False
        elif i == len(str_) - 4:
            return True
            
while True:
    try:
        code = input()
        if lenValid(code) and charValid(code) and repeatValid(code):
            print(ok)
        else:
            print(ng)
    except:
        break