t = eval(input('enter a tuple:'))

if type(t[0]) == type(t[1]):
    print('tuple is homogenous')
else:
    print('tuple is heterogenous')
