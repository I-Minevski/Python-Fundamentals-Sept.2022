import math


productivity=int(input())
workers=int(input())
competition=int(input())
biscuits=0
for i in range(1, 31):
    batch=productivity*workers
    if i%3==0:
        biscuits+=math.floor(batch*0.75)
    else:
        biscuits+=batch
print(f"You have produced {biscuits} biscuits for the past month.")
diff=abs(biscuits-competition)
if biscuits>competition:
    print(f"You produce {(diff/competition)*100:.2f} percent more biscuits.")
else:
    print(f"You produce {(diff/competition)*100:.2f} percent less biscuits.")