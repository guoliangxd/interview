def findLastWordLen(arg):
    if(arg.find(" ") == -1):
        return len(arg)
    substr = arg.split(' ')
    return len(substr[-1])
    

str = input()
print(findLastWordLen(str))