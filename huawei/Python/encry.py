import sys
def encry(str_):
    result = ''
    for char in str_:
        if char.islower():
            if char == 'z':
                result += 'A'
            else:
                result += chr(ord(char) + 1).upper()
        elif char.isupper():
            if char == 'Z':
                result += 'a'
            else:
                result += chr(ord(char) + 1).lower()
        elif char.isdecimal():
            if char == '9':
                result += '0'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char
    return result

def dencry(str_):
    result = ''
    for char in str_:
        if char.islower():
            if char == 'a':
                result += 'Z'
            else:
                result += chr(ord(char) - 1).upper()
        elif char.isupper():
            if char == 'A':
                result += 'z'
            else:
                result += chr(ord(char) - 1).lower()
        elif char.isdecimal():
            if char == '0':
                result += '9'
            else:
                result += chr(ord(char) - 1)
        else:
            result += char
    return result
    
while True:
    try:
        print(encry(input()))
        print(dencry(input()))
    except:
        break