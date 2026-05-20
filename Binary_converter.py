decimal_number = int(input())

if decimal_number == 0:
    print(0)
else:
    binary_string = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder) + binary_string
        decimal_number = decimal_number // 2
        
    print(binary_string)