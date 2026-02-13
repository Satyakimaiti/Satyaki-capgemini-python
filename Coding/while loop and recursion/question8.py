def lower_ch(s, i = 0):
    if i == len(s):
        return
    
    if s[i].islower():
        print(s[i], end =' ')
        
    lower_ch(s, i + 1)
    
lower_ch(input('enter a string: '))