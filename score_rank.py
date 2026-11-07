#成绩排序，分数由高到低
students=[
    {"name":"小明","score":85},
    {"name":"小红","score":95},
    {"name":"小蓝","score":78},
    {"name":"小绿","score":66},
    {"name":"小白","score":99}
]
#按成绩排名
ranked=sorted(students,key=lambda s:s["score"],reverse=True)
for i,s in enumerate(ranked,start=1):
    print(f"第{i}名：{s['name']} {s['score']}分")