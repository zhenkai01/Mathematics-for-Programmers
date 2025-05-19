def decimal2binary(n):
    if n == 0:
        return "0"

    binary = ""
    num = abs(n)
    while num > 0:
        binary = str(num%2) + binary
        num  //= 2
    return binary


test_number = [0, 5, 10, 42]
for number in test_number:
    print(decimal2binary(number))
