num = input('enter a integer:')

last_digit = ""

for ch in num:
    last_digit = ch
    
if last_digit.isdigit() and int(last_digit) % 2 == 0:
    print("Last digit is Even")
else:
    print("Last digit is Odd")