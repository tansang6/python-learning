#判断成绩等级
score=int(input("请输入成绩："))
#先判断成绩是否合法
if score>100 or score<0:
    print("分数不合法")
#合法成绩进行评级
elif score>=90:
    print("成绩为A")
elif score>=80:
    print("成绩为B")
elif score>=70:
    print("成绩为C")
elif score>=60:
    print("成绩为D")
else:
    print("成绩为F")  