#求1-100中所有偶数的和
#第一种方法：首先for循环遍历1-100，if判断是否为偶数，如果为偶数则累加，不是则跳过
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print(f"方式一：{total}")
#第二种方式：for循环以2为步长遍历1-100的数字，再累加
total=0
for i in range(2,101,2):
    total+=i
print(f"方式二：{total}")
#第三种方式：while循环
total=0
i=1
while i<=100:
    if i%2==0:
        total+=i
    i+=1
print(f"方法三：{total}")