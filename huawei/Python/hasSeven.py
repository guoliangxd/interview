def hasSeven(n):
    result = 0
    for i in range(1, n + 1):
        if '7' in str(i) or i % 7 == 0:
            result += 1
    return result

while True:
    try:
        n = int(input())
        print(hasSeven(n))
    except:
        break