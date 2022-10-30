total_sum=0
characters=int(input())
for i in range(characters):
    current=input()
    total_sum+=ord(current)
print(f"The sum equals: {total_sum}")