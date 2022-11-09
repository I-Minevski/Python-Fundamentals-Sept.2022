klass={}
count=int(input())
for i in range(count):
    name=input()
    grade=float(input())
    if name not in klass.keys():
        klass[name]=[]
        klass[name].append(0)
        klass[name].append(0)
    klass[name][0]+=grade
    klass[name][1]+=1
for (key, value) in klass.items():
    avrg=value[0]/value[1]
    if avrg>=4.5:
        print(f"{key} -> {avrg:.2f}")