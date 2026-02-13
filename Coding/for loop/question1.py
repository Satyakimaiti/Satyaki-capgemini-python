ls = eval(input('enter a list:'))

for item in ls:
    if type(item) == int:
        print(item)