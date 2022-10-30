numbers_list=list(map(int, input().split(", ")))
indices=[i for i in range(len(numbers_list)) if numbers_list[i]%2==0]
print(indices)