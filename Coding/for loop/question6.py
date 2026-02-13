s = input('enter a string:')

for ch in s:
    if ch.islower():
        if ord(ch) % 2 == 0:
            print(ch)
            
