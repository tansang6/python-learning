#输入身高（M）和体重（kg）
height=float(input("请输入身高（米）"))
weight=float(input("请输入体重（千克）"))
#计算BMI
bmi=weight/(height**2)
#输出BMI
print(f"你的BMI是{bmi:.2f}")
#判断BMI是否正常，小于18.5为偏瘦，大于24为偏胖，区间为正常
if bmi<18.5:
    print("偏瘦")
elif bmi<24:
    print("正常")
elif bmi<28:
    print("偏胖")
else:
    print("肥胖")