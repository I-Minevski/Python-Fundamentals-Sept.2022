primus=input()
secundus=input()
last_creation=primus
for i in range(len(primus)):
    temporis=secundus[:i+1] + primus[i+1::]
    if temporis!=last_creation:
        print(temporis)
    last_creation=temporis