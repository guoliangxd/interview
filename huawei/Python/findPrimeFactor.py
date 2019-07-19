num = int(input())

while num != 1:
    for i in range(2, num + 1):
        if num % i == 0:
            num = num // i
            print(str(i), end = ' ')
            break