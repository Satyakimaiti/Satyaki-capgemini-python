import math

def is_strong(num):
    original = num
    total = 0
    
    while num > 0:
        digit = num % 10
        total += math.factorial(digit)
        num = num // 10
        
    return total == original

num = int(input('enter a number:'))

if is_strong(num):
    print('Strong number')
else:
    print('not a strong number')
        