def is_perfect(num):
    total = 0
    
    for i in range(1, num):
        if num % i == 0:
            total += i
            
    return total == num

n = int(input('enter a number:'))

if is_perfect(n):
    print('perfect number')
else:
    print('not perfect number')
    
    