data = eval(input("Enter data: "))

if isinstance(data, (int, float, str, bool)):
    print("It is single value data")
else:
    print("It is not single value data")
