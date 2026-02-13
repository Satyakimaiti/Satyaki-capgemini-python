import math

def is_strong(num):
    original = num
    total = 0
    
    while num > 0:
        digit = num % 10
        total += math.factorial(digit)
        num //= 10
        
    return total == original


def nth_strong(n):
    count = 0
    num = 1
    
    while True:
        if is_strong(num):
            count += 1
            if count == n:
                return num   
        
        num += 1


a = int(input('enter a number: '))
result = nth_strong(a)
print(result)
