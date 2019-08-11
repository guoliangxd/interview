#python列表逆序的三种方式，list.reverse,reversed(),[::-1]
def getValue(name):
    count = {}
    result = 0
    name = name.lower()
    for char in name:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    values = list(count.values())
    values.sort()
    values.reverse()
    for i in range(len(values)):
        result += value[i] * values[i]
    return result

value = []
for i in range(26):
    value.append(26 - i)
    
while True:
    try:
        n = int(input())
        for i in range(n):
            print(getValue(input()))
    except:
        break
        
            