def valid(a):
    is_valid=True
    if len(a)<6 or len(a)>10:
        is_valid=False
        print("Password must be between 6 and 10 characters")
    count_digits=0
    for i in a:
        if "a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9":
            pass
        else:
            is_valid=False
            print("Password must consist only of letters and digits")
            break
        if "0"<=i<="9":
            count_digits+=1
    if count_digits<2:
        is_valid=False
        print("Password must have at least 2 digits")
    return is_valid


password=input()
if valid(password)==True:
    print(f"Password is valid")