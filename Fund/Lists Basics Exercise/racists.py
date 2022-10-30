time_left=0
time_right=0
sequence=input().split(" ")
sequence=[float(x) for x in sequence]
for i in range((len(sequence)//2)):
    if sequence[i]!=0:
        time_left+=sequence[i]
    else:
        time_left*=0.8
for i in range(len(sequence)-1, len(sequence)//2, -1):
    if sequence[i]!=0:
        time_right+=sequence[i]
    else:
        time_right*=0.8
if time_left<time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")