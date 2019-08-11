#python表达时求值可以直接用内置函数eval，也可用栈来解决
#TODO:再写一个用栈实现的版本
while True:
    try:
        print(eval(input()))
    except:
        break