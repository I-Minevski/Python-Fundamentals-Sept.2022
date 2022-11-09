word=''.join(input().split(" "))
chars={}
for i in word:
    if i not in chars.keys():
        chars[i]=0
    chars[i]+=1
for (key, value) in chars.items():
    print(f"{key} -> {value}")