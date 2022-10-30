number_lines=int(input())
tank=0
for line in range(number_lines):
    litres=int(input())
    if tank+litres>255:
        print("Insufficient capacity!")
    else:
        tank+=litres
print(tank)
