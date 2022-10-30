line1=input().split(" ")
line2=input().split(" ")
line3=input().split(" ")
winner=0
if "1" not in line1 and "0" not in line1:
    winner=2
elif "1" not in line2 and "0" not in line2:
    winner=2
elif "1" not in line3 and "0" not in line3:
    winner=2
elif "2" not in line1 and "0" not in line1:
    winner=1
elif "2" not in line2 and "0" not in line2:
    winner=1
elif "2" not in line3 and "0" not in line3:
    winner=1
elif line1[0]==line2[1]==line3[2]=="1":
    winner=1
elif line1[0]==line2[1]==line3[2]=="2":
    winner=2
elif line1[2]==line2[1]==line3[0]=="1":
    winner=1
elif line1[2]==line2[1]==line3[0]=="2":
    winner=2
for i in range(3):
    if line3[i]==line1[i]==line2[i]=="1":
        winner=1
    elif line3[i]==line1[i]==line2[i]=="2":
        winner=2
if winner==0:
    print("Draw!")
if winner==1:
    print("First player won")
if winner==2:
    print("Second player won")