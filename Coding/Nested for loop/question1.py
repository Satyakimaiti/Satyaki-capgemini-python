s = 'power star'

op = {}

for word in s.split():
    count = 0
    for _ in word:
        count += 1
    op[word] = count
    
print(op)