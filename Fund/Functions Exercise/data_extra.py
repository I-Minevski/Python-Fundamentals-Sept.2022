def operations(a, b):
    if a=="int":
        print(int(b)*2)
    if a=="real":
        print(f"{float(b)*1.5:.2f}")
    if a=="string":
        print(f"${b}$")
        
        
type=input()
data=input()
operations(type, data)