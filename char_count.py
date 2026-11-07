#字符统计，统计每个字符出现的次数
text=input("请输入一段文字：")
counts={}
#遍历text文本，每出现一次字符，对应counts中键对应的值+1
for ch in text:
    if ch in counts:
        counts[ch]+=1
    else:
        counts[ch]=1    #字典中键不存在时赋1，存在时+1(相当于第一次出现该字母仅将他记录，第二次见到该字母才会开始计数)
for ch,n in counts.items():
    print(f"{ch}:{n}")   #这一步是打印每个字符对应的出现次数
#如果想单独查询
#target=input("想要查询的字符:")
#print(f"{target}出现了{counts.get(target,0)}次")