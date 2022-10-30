sequence=input().split(" ")
sequence=[int(x) for x in sequence]
word=input()
word_list=[]
for i in range(len(word)):
    word_list.append(word[i])
message=""
for i in range(len(sequence)):
    index=0
    while sequence[i]>0:
        index+=sequence[i]%10
        sequence[i]//=10
    if index>len(word_list)-1:
        while index>len(word_list)-1:
            index-=(len(word_list))
    message+=word_list[index]
    del word_list[index]
print(message)