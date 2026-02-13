def natural(n, i = 1):
    if i > n:
        return
    print(i, end = ' ')
    natural(n, i + 1)
    
natural(int(input('enter n: ')))