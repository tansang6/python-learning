#猜数字游戏，生成随机数，用户输入数字，程序判断大小并输出，最终猜对时输出总次数
import random

answer = random.randint(1,100) #生成随机数
count = 0 #记录猜测次数
while True:
    guess=int(input("请输入猜测的数字："))
    count+=1
    if guess>answer:
        print("大于真实答案")
    elif guess<answer:
        print("小于真实答案")
    else:
        print(f"猜对了，一共猜了{count}次")
        break
