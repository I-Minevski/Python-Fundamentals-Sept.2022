electrons=int(input())
shell=1
atom=[]
while electrons>0:
    if electrons>2*shell*shell:
        atom.append(2*shell*shell)
        electrons-=2*shell*shell
    else:
        atom.append(electrons)
        electrons=0
    shell+=1
print(atom)