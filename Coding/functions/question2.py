import math

def is_strong(n):
    original = n
    total = 0
    
    while n > 0:
        digit = n % 10
        total += math.factorial(digit)
        n = n // 10
        
    return total == original


def strong_in_range(a, b):
    for i in range(a, b+1):
        if is_strong(i):
            print(i, end=' ')
            
num1 = int(input('enter a number:'))
num2 = int(input('enter a number2:'))
strong_in_range(num1, num2)