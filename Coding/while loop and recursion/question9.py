def vowel(s, i = 0):
    if i == len(s):
        return
    
    if s[i].lower() in 'aeiou':
        print(s[i], end = ' ')
        
    vowel(s, i + 1)
    
vowel(input('enter a string: '))