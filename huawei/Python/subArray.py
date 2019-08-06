#l剩下数组里的元素，肯定在两个数组之一，利用递归求解
def isExist(s1, s2, other, index):
    if index == len(other):
        if s1 == s2:
            return True
        else:
            return False
    else:
        return isExist(s1 + other[index], s2, other, index + 1) or isExist(s1, s2 + other[index], other, index + 1)
    
while True:
    try:
        n = int(input())
        five = 0
        three = 0
        others = []
        nums = input().split()
        for num in nums:
            num = int(num)
            if num % 5 == 0:
                five += num
            elif num % 3 == 0:
                three += num
            else:
                others.append(num)
        if isExist(five, three, others, 0):
            print('true')
        else:
            print('false')
    except:
        break