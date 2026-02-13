def table(n, i = 1):
    if i > 10:
        return
    
    print(n, "X", i, "=", n * i)
    table(n, i+1)
    
table(int(input('enter number: ')))