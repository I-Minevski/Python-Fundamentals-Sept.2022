seq=input().split(" ")
while True:
    command=input()
    if command=="3:1":
        break
    com_list=command.split(" ")
    if "merge" in com_list:
        start=int(com_list[1])
        finish=int(com_list[2])
        if finish>len(seq)-1:
            finish=len(seq)-1
        new_string=""
        for i in range(start, finish+1):
            new_string+=seq[i]
        del seq[start:finish+1]
        seq.insert(start, new_string)
    if "divide" in com_list:
        index=int(com_list[1])
        parts=int(com_list[2])
        guz=seq[index]
        if len(seq[index])%parts==0:
            diff=len(seq[index])//parts
            for i in range(0, len(guz), diff):
                new_string=guz[i:i+diff]
                seq.insert(index, new_string)
                index+=1
            seq=[x for x in seq if x!=guz]
        else:
            diff=len(seq[index])//parts
            if diff<1:
                diff=1
            count=1
            for i in range(0, len(guz), diff):
                if count==parts:
                    new_string=guz[i::]
                    seq.insert(index, new_string)
                    break
                new_string=guz[i:i+diff]
                seq.insert(index, new_string)
                index+=1
                count+=1
            seq=[x for x in seq if x!=guz]
    print(' '.join(x for x in seq))