mnoj=input()
num_list=mnoj.split(" ")
for i in range(len(num_list)):
    num_list[i]=int(num_list[i])*(-1)
print(num_list)