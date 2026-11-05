#判断年份是否是闰年，能被4整除且不能被100整除，或者能被400整除
year=int(input("请输入年份："))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")