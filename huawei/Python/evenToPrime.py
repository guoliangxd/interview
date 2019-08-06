def isPrime(num):
    if num == 1:
        return True
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        flag = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        return flag
        
while True:
    try:
        even = int(input())
        for i in range(even // 2, 0, -1):
            if isPrime(i):
                other = even - i
                if isPrime(other):
                    print(i)
                    print(other)
                    break
    except:
        break