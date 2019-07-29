import sys

out = [] # 用于按顺序存储每个不重复的记录
num = {} # 用于存储每条记录的重复次数
 
while True:
    input_ = sys.stdin.readline()[:-1].strip() #readline与input比会读取换行符,还是用try except更稳妥
    if input_ == '':
        break
    record, lines = input_.split()
    if '\\' in record:
        name = record.split('\\')[-1][-16:]
    else:
        name = record[-16:]
    item = name + ' ' + lines
    if item not in num:
        num[item] = 1
        out.append(item)
    else:
        num[item] += 1
         
for item in out[-8:]:
    print(item+' '+str(num[item]))