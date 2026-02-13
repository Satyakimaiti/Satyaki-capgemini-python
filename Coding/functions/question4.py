def is_armstrong(num):
    original = num
    power = len(str(num))
    total = 0
    
    while num > 0:
        digit = num % 10
        total += digit ** power
        num = num // 10
        
    return total == original

n = int(input('enter a number:'))

if(is_armstrong(n)):
    print('It is an armstrong number')
else:
    print('it is not an armstrong number')