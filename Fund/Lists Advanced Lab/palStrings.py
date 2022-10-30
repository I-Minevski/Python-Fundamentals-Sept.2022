def pal(i):
        is_pal=True
        buff=0
        br=len(i)
        while br>0:
            if i[buff]!=i[len(i)-buff-1]:
                is_pal=False
                break
            br-=1
        return is_pal


strings=input().split(" ")
search=input()
palindromes=[]
for i in range(len(strings)):
    if pal(strings[i])==True:
        palindromes.append(strings[i])
count=palindromes.count(search)
print(palindromes)
print(f"Found palindrome {count} times")