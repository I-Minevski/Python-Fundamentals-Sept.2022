words=[word.lower() for word in input().split(" ")]
dict={}
for word in words:
    if word not in dict:
        dict[word]=0
    dict[word]+=1
for (key, value) in dict.items():
    if value%2!=0:
        print(key, end=" ")