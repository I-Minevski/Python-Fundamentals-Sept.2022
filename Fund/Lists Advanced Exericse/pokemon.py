seq=[int(number) for number in input().split(" ")]
captured=0
while len(seq)>0:
    index=int(input())
    if index<0:
        pokemon=seq[0]
        seq[0]=seq[len(seq)-1]
    elif index>=len(seq):
        pokemon=seq[len(seq)-1]
        seq[len(seq)-1]=seq[0]
    else:
        pokemon=seq[index]
        del seq[index]
    captured+=pokemon
    seq=list(map(lambda x: x+pokemon if(x<=pokemon) 
            else x-pokemon,
            seq))
print(captured)