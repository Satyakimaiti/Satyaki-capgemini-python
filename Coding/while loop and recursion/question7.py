def even_ind(s, i = 0):
    if i == len(s):
        return
    
    if i % 2 == 0:
        print(s[i])
        
    even_ind(s, i + 1)
    
even_ind(input('enter a string:'))