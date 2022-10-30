def chat(arr, mes):
    arr.append(mes)


def delete(arr, mes):
    if mes in arr:
        arr.remove(mes)


def edit(arr, mes1, mes2):
    index=arr.index(mes1)
    arr[index]=mes2


def pin(arr, mes):
    if mes in arr:
        arr.remove(mes)
        arr.append(mes)


def spam(arr, mes_arr):
    arr.extend(mes_arr)


history=[]
while True:
    command=input()
    if command=="end":
        break
    com_list=command.split(" ")
    message=com_list[1]
    if "Chat" in com_list:
        chat(history, message)
    if "Delete" in com_list:
        delete(history, message)
    if "Edit" in com_list:
        edited=com_list[2]
        edit(history, message, edited)
    if "Pin" in com_list:
        pin(history, message)
    if "Spam" in com_list:
        spam_hist=[com_list[i] for i in range(1, len(com_list))]
        spam(history, spam_hist)
print('\n'.join(x for x in history))