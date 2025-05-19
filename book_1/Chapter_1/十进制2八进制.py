def decimal2octal(n):
    if n == 0:
        return "0"

    octal = ""
    num = abs(n)
    while num > 0:
        octal = str(num%8) + octal
        num  //= 8
    return octal


test_number = [0, 5, 10, 42, 100, 255]
for number in test_number:
    print(decimal2octal(number))
