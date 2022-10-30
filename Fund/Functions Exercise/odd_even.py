def sum_of_even(a):
    b=a
    sum_even=0
    while b>0:
        digit=b%10
        if digit%2==0:
            sum_even+=digit
        b//=10
    return sum_even

def sum_of_odd(a):
    b=a
    sum_odd=0
    while b>0:
        digit=b%10
        if digit%2!=0:
            sum_odd+=digit
        b//=10
    return sum_odd
        
number=int(input())
print(f"Odd sum = {sum_of_odd(number)}, Even sum = {sum_of_even(number)}")