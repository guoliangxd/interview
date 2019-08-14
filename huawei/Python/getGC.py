def getGC(st):
    n = 0
    for char in st:
        if char == 'C' or char == 'G':
            n += 1
    return n
while True:
    try:
        DNA = input()
        ln = int(input())
        maxLen = 0
        subDNA = ''
        for i in range(len(DNA) - ln + 1):
            sub = DNA[i : i + ln]
            if getGC(sub) > maxLen:
                maxLen = getGC(sub)
                subDNA = sub
        print(subDNA)
    except:
        break