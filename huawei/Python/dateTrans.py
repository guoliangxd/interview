normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    try:
        year = int(input())
        mon = int(input())
        day = int(input())
        n = day
        if mon > 2 and ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
            n += 1
        for i in range(mon - 1):
            n += normal[i]
        print(n)
    except:
             break
                        