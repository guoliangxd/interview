#Python会自动进行题目要求的处理
while True:
    try:
        st, ln = input().split()
        print(st[ : int(ln)])
    except:
        break