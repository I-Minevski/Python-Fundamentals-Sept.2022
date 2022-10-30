def palindrome(a):
    for i in a:
        is_pal=True
        buff=0
        br=len(i)
        while br>0:
            if i[buff]!=i[len(i)-buff-1]:
                is_pal=False
                print(is_pal)
                break
            br-=1
        if is_pal==True:
            print(is_pal)

sequence=input().split(", ")
palindrome(sequence)