#有规律，首项为m*m-m+1，共m项
while True:
    try:
        m = int(input())
        first = m * (m - 1) + 1
        print(str(first), end = '')
        for i in range(m - 1):
            print('+' + str(first + 2 + 2 * i), end = '')
        print()
    except:
        break