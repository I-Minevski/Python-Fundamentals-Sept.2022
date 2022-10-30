balls=int(input())
highest_value=0
for b in range(balls):
    weight=int(input())
    time=int(input())
    quality=int(input())
    value=(weight/time)**quality
    if value>highest_value:
        highest_value=value
        highest_weight=weight
        highest_time=time
        highest_quality=quality
print(f"{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})")