#TODO:复杂度太高，要改用马拉车算法
def isPalindRome(st):
    return st == st[::-1]#返回逆序字符串
while True:
    try:
        st = input()
        finish = False
        for maxLen in range(len(st), 0, -1):
            for i in range(len(st)):
                if i + maxLen <= len(st) and isPalindRome(st[i : i + maxLen]):
                    print(maxLen)
                    finish = True
                    break
            if finish == True:
                break
    except:
        break
                    