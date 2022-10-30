import math
cnt=int(input())
yrs=cnt*100
days=math.floor(yrs*365.2422)
hrs=days*24
mts=hrs*60
print(f"{cnt} centuries = {yrs} years = {days} days = {hrs} hours = {mts} minutes")