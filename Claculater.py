def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
print("chose your operation")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
type = int(input("Enter yor selcted operation(1,2,3,4): "))
a=int(input("Enter first number: "))
s=int(input("enter second number: "))
if type==1:
    print(a," + ", s," = ", add(a, s))
elif type==2:
    print(a," - ", s," = ", subtract(a, s))
elif type==3:
    print(a," x ", s," = ", multiply(a, s))
elif type==4:
    print(a," / ", s," = ", divide(a, s))
else:
    print("Invalid option")