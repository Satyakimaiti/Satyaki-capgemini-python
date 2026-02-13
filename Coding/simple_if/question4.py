num = int(input("Enter a number: "))

if num % 9 == 0 or num % 6 == 0:
    print("Cube is:", num ** 3)
else:
    print("Number is not divisible by 9 or 6")
