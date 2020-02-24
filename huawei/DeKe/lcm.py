def findMaxDivisor(m, n):
    if n == 0:
        return m
    else:
        return findMaxDivisor(n, m % n)
    
data = input().split()
a = int(data[0])
b = int(data[1])
maxDivisor = findMaxDivisor(a, b)
print(a * b / maxDivisor)