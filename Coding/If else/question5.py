a = eval(input('enter first value:'))
b = eval(input('enter second value:'))

if id(a) == id(b):
    print('both are pointing to same memory')
else:
    print('not pointing to same memory')