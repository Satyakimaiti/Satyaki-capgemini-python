s = input('enter a string:')
reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string
    
print('reversed string is:', reversed_string)