def print_ch(s, i=0):
    if(i == len(s)):
        return
    
    print(s[i])
    print_ch(s, i + 1)
    
print_ch(input('enter a string: '))