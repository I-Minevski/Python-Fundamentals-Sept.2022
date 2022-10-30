def cypher(arr):
    num=[char for char in arr if not 'a'<=char<='z']
    arr=list(filter(lambda x: x not in num, arr))
    num=int(''.join(char for char in num))
    arr.insert(0, chr(num))
    arr[1], arr[len(arr)-1] = arr[len(arr)-1], arr[1]
    return ''.join(char for char in arr)
    

gibberish=input().split(" ")
printable=list(map(lambda x: cypher(x), gibberish))
print(' '.join(word for word in printable))