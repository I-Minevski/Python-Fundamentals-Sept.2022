first_seq=input().split(", ")
second_seq=input().split(", ")
substrings=[]
for i in first_seq:
    for j in second_seq:
        if i in j:
            substrings.append(i)
            break
print(substrings)

#substrings=[first for first in first_seq if any(first in second for second in second_seq)]
#mn nasrano znam. ama e po kratko