ls = eval(input('enter a list:'))

for item in ls:
    if type(item) == int:
        if item % 2 == 0:
            print(item)
            
