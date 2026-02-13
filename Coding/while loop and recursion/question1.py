def print_python(n):
    if n == 0:
        return
    
    print('python')
    print_python(n-1)

print_python(5)