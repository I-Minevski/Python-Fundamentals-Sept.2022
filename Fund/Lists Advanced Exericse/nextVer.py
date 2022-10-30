version=[int(number) for number in input().split(".")]
if version[-1]!=9:
    version[-1]+=1
elif version[-2]!=9:
    version[-1]=0
    version[-2]+=1
else:
    version[-3]+=1
    version[-2]=0
    version[-1]=0
new_version='.'.join(str((number) for number in version))
print(new_version)