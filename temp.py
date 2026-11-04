#输入温度（℃），将其转化为华氏温度（℉），并输出
celsius=float(input("请输入温度（℃）："))
fahrenheit=celsius*9/5+32
print(f"{celsius:.1f}℃ = {fahrenheit:.1f}℉")