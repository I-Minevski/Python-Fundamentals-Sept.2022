import sys
sequence=input().split(" ")
sequence=[int(x) for x in sequence]
different=[]
for i in range(len(sequence)):
    if sequence[i] not in different:
        different.append(sequence[i])
pure=True
if len(different)>1:
    pure=False
while True:
    command=input()
    if command=="end":
        print(sequence)
        break
    com_list=command.split(" ")
    
    
    if com_list[0]=="exchange":
        index=int(com_list[1])
        if index>len(sequence)-1 or index<0:
            print("Invalid index")
        else:
            sequence=sequence[index+1::] + sequence[:index+1:]
    
    
    elif com_list[0]=="max":
        if pure==True:
            print("No matches")
        maxel=-sys.maxsize
        index=0
        
        if com_list[1]=="even":
            for i in range(len(sequence)-1, -1, -1):
                if sequence[i]%2==0 and sequence[i]>maxel:
                    maxel=sequence[i]
                    index=i
            if maxel==-sys.maxsize:
                print("No matches")
            else:
                print(index)
        
        if com_list[1]=="odd":
            for i in range(len(sequence)-1, -1, -1):
                if sequence[i]%2!=0 and sequence[i]>maxel:
                    maxel=sequence[i]
                    index=i
            if maxel==-sys.maxsize:
                print("No matches")
            else:
                print(index)
    
    
    elif com_list[0]=="min":
        if pure==True:
            print("No matches")
        minel=sys.maxsize
        index=0
        
        if com_list[1]=="even":
            for i in range(len(sequence)-1, -1, -1):
                if sequence[i]%2==0 and sequence[i]<minel:
                    minel=sequence[i]
                    index=i
            if minel==sys.maxsize:
                print("No matches")
            else:
                print(index)
        
        if com_list[1]=="odd":
            for i in range(len(sequence)-1, -1, -1):
                if sequence[i]%2!=0 and sequence[i]<minel:
                    minel=sequence[i]
                    index=i
            if minel==sys.maxsize:
                print("No matches")
            else:
                print(index)
    
    
    elif com_list[0]=="first":
        count=int(com_list[1])
        if count>len(sequence):
            print("Invalid count")
            continue
        printing=[]
        
        if com_list[2]=="even":
            for i in range(len(sequence)):
                if len(printing)==count:
                    break
                if sequence[i]%2==0:
                    printing.append(sequence[i])
        
        if com_list[2]=="odd":
            for i in range(len(sequence)):
                if len(printing)==count:
                    break
                if sequence[i]%2!=0:
                    printing.append(sequence[i])
        print(printing)
        
        
    elif com_list[0]=="last":
        count=int(com_list[1])
        if count>len(sequence):
            print("Invalid count")
            continue
        printing=[]
        
        if com_list[2]=="even":
            for i in range(len(sequence)-1, -1, -1):
                if len(printing)==count:
                    break
                if sequence[i]%2==0:
                    printing.append(sequence[i])
        
        if com_list[2]=="odd":
            for i in range(len(sequence)-1, -1, -1):
                if len(printing)==count:
                    break
                if sequence[i]%2!=0:
                    printing.append(sequence[i])
        printing.reverse()
        print(printing)