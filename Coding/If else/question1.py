data = eval(input('enter any data:'))

if isinstance(data, (list, dict, set, bytearray)):
    print('mutable data type')
else:
    print('Immutable data type')
    
