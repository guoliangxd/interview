def isPerfect(n):
    divisor = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        return True
    else:
        return False

while True:
    try:
        num = int(input())
        result = 0
        for i in range(1, num + 1):
            if isPerfect(i):
                result += 1
        print(result)
    except:
        break