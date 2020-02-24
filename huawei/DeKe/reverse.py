while True:
    try:
        data = input().split()
        print(' '.join(data[::-1]))
    except:
        break