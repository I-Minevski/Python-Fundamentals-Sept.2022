judge={"results" : {}, "submissions" : {}}
while True:
    info=input().split("-")
    if info[0]=="exam finished":
        break
    if "banned" in info:
        username=info[0]
        del judge["results"][username]
    else:
        username=info[0]
        language=info[1]
        points=int(info[2])
        if username not in judge["results"].keys():
            judge["results"][username]=points
        else:
            if judge["results"][username]<points:
                judge["results"][username]=points
        if language not in judge["submissions"].keys():
            judge["submissions"][language]=0
        judge["submissions"][language]+=1
print("Results:")
for (key, value) in judge["results"].items():
    print(f"{key} | {value}")
print("Submissions:")
for (key, value) in judge["submissions"].items():
    print(f"{key} - {value}")