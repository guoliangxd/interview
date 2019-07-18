# python没有++，--
str = input()
char = input()
str = str.lower()
char = char.lower()
count = 0
for i in range(len(str)):
    if(str[i] == char):
        count += 1
print(count)
