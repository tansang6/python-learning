#输入两个数，分别计算他们的和、差、积、商
a=float(input("请输入第一个数："))
b=float(input("请输入第二个数："))
print(f"它们的和是{a+b}")
print(f"它们的差是{a-b}")
print(f"它们的积是{a*b}")
#判断除数是否为0，不为0则正常计算，为0则提示除数为0，无法计算
if b!=0:
    print(f"它们的商是{a/b:.2f}")
else:
    print("除数不能为0，无法计算")