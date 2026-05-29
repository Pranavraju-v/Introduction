age=float(input("Enter age: "))
x=(" ")
if age % 1 != 0:
    print("Enter a whole number")
elif age % 2 == 0:
    print("even")
elif age % 2 == 1:
    print("odd")
else:
    try:
        ValueError
    except:
        print("Enter a number")
 