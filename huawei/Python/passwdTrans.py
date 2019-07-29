def passwdTrans(passwd):
    result = ''
    for char in passwd:
        if char.isupper():
            if char == 'Z':
                result += 'a'
            else:
                 result += chr(ord(char.lower()) + 1)
        elif char.islower():
             if char in 'abc':
                 result += '2'
             elif char in 'def':
                 result += '3'
             elif char in 'ghi':
                 result += '4'
             elif char in 'jkl':
                 result += '5'
             elif char in 'mno':
                 result += '6'
             elif char in 'pqrs':
                 result += '7'
             elif char in 'tuv':
                 result += '8'
             elif char in 'wxyz':
                 result += '9'
        else:
             result += char
    return result
            
while True:
    try:
        passwd = input()
        print(passwdTrans(passwd))
    except:
        break