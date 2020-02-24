def isPrime(i):
    if i < 2:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                return False
        return True

while(True):
    result = 'end'
    data = int(input())
    if data == 0:
        print(result)
        break
    else:
        if data <= 3:
            result = 0
        else:
            total = 0
            for i in range(2, data // 2 + 1):
                if isPrime(i) and isPrime(data - i):
                    total += 1
            result = total
    print(result)