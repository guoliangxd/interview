import sys
for str in sys.stdin:
    dir = {}
    for i in range(len(str)):
        if str[i] not in dir:
            dir[str[i]] = 1
        else:
            dir[str[i]] += 1

    min = len(str)
    for v in dir.values():
        if v < min:
            min = v

    for i in range(len(str)):
        if dir[str[i]] == min:
            continue
        else:
            print(str[i], end='')

    print()
