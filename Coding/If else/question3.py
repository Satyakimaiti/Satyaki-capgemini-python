lst = eval(input("Enter a list: "))

n = len(lst)

if n == 0:
    print("Empty list")
else:
    mid_index = n // 2
    mid_value = lst[mid_index]

    if lst.count(mid_value) > 1:
        print("List consists of the middle value")
    else:
        print("List does not consist of the middle value")
