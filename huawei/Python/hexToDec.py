import sys

def hexToDec(hexStr):
    if len(hexStr) < 3:
        return None
    else:
        return int(hexStr, 16)  

for line in sys.stdin:
    print(hexToDec(line))