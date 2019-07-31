while True:
    try:
        sen = input() + ' '
        begin = 0
        words = []
        for i in range(len(sen)):
            if sen[i].isalpha():
                continue
            else:
                if i > begin:
                    words.append(sen[begin : i])
                    begin = i + 1
                else:
                    begin += 1
        for i in range(len(words) - 1):
            print(words[-1-i], end = ' ')
        print(words[0])
    except:
        break