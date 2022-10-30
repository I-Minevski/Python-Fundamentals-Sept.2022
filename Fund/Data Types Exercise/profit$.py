from xml.dom.pulldom import default_bufsize


companions=int(input())
days=int(input())
coins=0
for day_index in range(1, days+1):
    if day_index%10==0:
        companions-=2
    if day_index%15==0:
        companions+=5
    coins+=50
    coins-=2*(companions)
    if day_index%3==0:
        coins-=3*(companions)
    if day_index%5==0:
        coins+=20*companions
    if day_index%15==0:
        coins-=2*(companions)
print(f"{companions} companions received {int(coins//companions)} coins each.")
    