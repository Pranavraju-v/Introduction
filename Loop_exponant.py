base = int(input("Enter number: "))
exponent = int(input("Enter exponant"))

result = 1

for i in range(exponent):
    result = result * base

print(result)