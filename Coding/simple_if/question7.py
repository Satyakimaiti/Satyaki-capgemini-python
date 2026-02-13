data = input('enter data:')

try:
    value = float(data)
    if '.' in data:
        print('it is a float')
    else:
        print('it is not a float')
except:
    print('it is not a float')