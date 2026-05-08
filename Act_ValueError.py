try:
   num=int(input("Enter a number: "))
   print("The number entered is: ", num)
except ValueError as ex:
    print("Exeption:", ex)