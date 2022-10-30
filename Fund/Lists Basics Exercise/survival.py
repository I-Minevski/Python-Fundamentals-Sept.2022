seq=input()
sequence=[]
sequence=seq.split(" ")
sequence=[int(x) for x in sequence]
removed=int(input())
while removed>0:
    sequence.remove(min(sequence))
    removed-=1
sequence=[str(x) for x in sequence]
print(", ".join(sequence))