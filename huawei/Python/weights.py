def weights(n,weight,nums):
    res = set()
    for i in range(nums[0]+1):
        res.add(i*weight[0])
    for i in range(1,n):#加入剩余n-1个砝码的各种组合与现有组合的组合
        tmp = list(res)
        for j in range(1,nums[i]+1):#加0的的重量已经有了，从1开始
            for wt in tmp:
                res.add(wt+j*weight[i])
    return len(res)
while True:
    try:
        n = int(input())
        weight = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(weights(n,weight,nums))
    except:
        break