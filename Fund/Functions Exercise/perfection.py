def perfect(a):
    divisors=[]
    for i in range(1, a):
        if a%i==0:
            divisors.append(i)
    if a==sum(divisors):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number=int(input())
perfect(number)