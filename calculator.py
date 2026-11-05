#简易计算器，能够计算+、-、*、/
a=float(input("请输入第一个数："))
b=float(input("请输入第二个数："))
op=input("请输入运算符（+ - * /）：")
#先判断运算符是否合规
if op not in "+-*/":
    print("暂时不支持该运算符")
elif op =="+":
    print (f"{a}+{b}={a+b}")
elif op=="-":
    print(f"{a}-{b}={a-b}")
elif op=="*":
    print(f"{a}*{b}={a*b}")
elif op=="/":
    if b==0:
        print("除数不能为0")
    else:
        print(f"{a}/{b}={a/b:.2f}")