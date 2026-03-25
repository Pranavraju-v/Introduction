thing=str(input("Enter singel character only: "))
if len(thing)!=1:
    print("Please enter 1 character only!")
ASCII_value=ord(thing)
print("The ASCII value is",ASCII_value)
if ASCII_value >= 65 and ASCII_value <= 90:
    print("This is an uppercase letter")
elif ASCII_value >= 97 and ASCII_value <= 122:
     print("This is a lowercase letter")
elif ASCII_value >= 48 and ASCII_value <= 57:
    print("This is a number")
elif ASCII_value == 32:
    print("The spacebar")
else:
    print("This is a special charater")
