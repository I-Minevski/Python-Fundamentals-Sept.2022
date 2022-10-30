def positive(arr):
    return [num for num in arr if num>=0]


def negative(arr):
    return [num for num in arr if num<0]


def even(arr):
    return [num for num in arr if num%2==0]


def odd(arr):
    return [num for num in arr if num%2!=0]


sequence=[int(number) for number in input().split(", ")]

print(f"Positive: {', '.join(str(num) for num in positive(sequence))}")
print(f"Negative: {', '.join(str(num) for num in negative(sequence))}")
print(f"Even: {', '.join(str(num) for num in even(sequence))}")
print(f"Odd: {', '.join(str(num) for num in odd(sequence))}")