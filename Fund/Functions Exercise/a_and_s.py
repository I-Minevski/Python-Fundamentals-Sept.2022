from ast import Num


def sum_numbers(a, b):
    return a+b

def subtract(a, b):
    return a-b

def add_and_subtract(a, b, c):
    sum_of_two=sum_numbers(a, b)
    return subtract(sum_of_two, c)

num1=int(input())
num2=int(input())
num3=int(input())
print(add_and_subtract(num1, num2, num3))