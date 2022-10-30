seq=[word for word in input().split(" ")]
filtered=[word for word in seq if len(word)%2==0]
print('\n'.join(word for word in filtered))