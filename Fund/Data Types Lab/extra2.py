is_prime=True
number=int(input())
for i in range(2, number):
    if number%i==0:
        is_prime=False
print(is_prime)