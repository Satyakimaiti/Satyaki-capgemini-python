def is_armstrong(num):
    original = num
    power = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    return total == original


def nth_armstrong(n):
    count = 0
    num = 1

    while True:
        if is_armstrong(num):
            count += 1
            if count == n:
                return num
        num += 1


k = int(input("Enter n: "))
print(nth_armstrong(k))
