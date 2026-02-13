s = 'power star'

op = {}

for word in s.split():
    vcount = 0
    for ch in word:
        if ch in 'aeiou':
            vcount += 1
            
    op[word] = vcount
    
print(op)