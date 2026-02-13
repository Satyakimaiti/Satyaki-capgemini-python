n = int(input("Enter number of key-value pairs: "))

d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Required key-value pairs:")

for k in d:
    if type(k) == str and k.isalpha() and d[k].lstrip('-').isdigit():
        print(k, ":", int(d[k]))
