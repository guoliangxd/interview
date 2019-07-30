def ipToDec(ip):
    subIP = ip.split('.')
    binIP = ('00000000' + bin(int(subIP[0]))[2 : ])[-8 : ] + ('00000000' + bin(int(subIP[1]))[2 : ])[-8 : ] + ('00000000' + bin(int(subIP[2]))[2 : ])[-8 : ] + ('00000000' + bin(int(subIP[3]))[2 : ])[-8 : ]
    return int(binIP, 2)

def decToIP(dec):
    binIP = bin(int(dec))[2 : ]
    binIP = ('00000000000000000000000000000000'+ binIP)[-32 : ]
    ip = ''
    for i in range(4):
        ip += str(int(binIP[8 * i : 8 * i + 8], 2)) + '.'
    return ip[ : -1]

while True:
    try:
        print(ipToDec(input()))
        print(decToIP(input()))
    except:
        break
