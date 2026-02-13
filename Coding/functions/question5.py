def is_armstrong(num):
    original = num
    power = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    return total == original


def armstrong_in_range(start, end):
    for n in range(start, end + 1):
        if is_armstrong(n):
            print(n, end=" ")


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

armstrong_in_range(a, b)
