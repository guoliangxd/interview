# 返回最后一个单词长度
def findLastWordLen(arg):
    """ 将输入的字符串去掉首尾空格后按空格分隔为字串列表，返回最后一个字串的长度"""
    if(arg.find(" ") == -1):
        #输入无空格时直接返回字符串长度
        return len(arg)
    arg = arg.strip()
    substr = arg.split(' ')
    return len(substr[-1])
    

str = input()
print(findLastWordLen(str))
