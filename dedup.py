#列表去重（不改变顺序，去掉重复值）
nums=[3,1,5,4,1,2,5,8,9,5,6]
result=[]
for n in nums:
    if n not in result:    #result没有的加进去，出现过的不加，同时顺序不变
        result.append(n)
print(result)