n=int(input())
syno={}
for i in range(n):
    word=input()
    synonym=input()
    if word not in syno.keys():
        syno[word]=[]
    syno[word].append(synonym)
for (key, value) in syno.items():
    print(f"{key} - {', '.join(x for x in value)}")