#利用递归求解，某方向为0时只有一种可能
def getRouts(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        return getRouts(n - 1, m) + getRouts(n, m - 1)
    
while True:
    try:
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        print(getRouts(n, m))
    except:
        break