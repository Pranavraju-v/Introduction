def add(x, y):
    return(x+y)
def subtract(x, y):
    return(x-y)
def multiply(x, y):
    return(x*y)
def divide(x, y):
    return(x/y)

type=input("Enter type(subtraction,addition,multiplication,division): ")

try:
    x=int(input("Enter the first number: "))
    y=int(input("Enter the seconed number: "))
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("A number cant be divided by 0")

if type=="subtraction":
    print("x", + "-" + , "y" ,"=" +, subtract(x, y))
elif type=="addition":
    print("x", + "+" + "y" "=" + , add(x, y))
elif type=="multiplication":
    print("x",+"*"+, "y",+ "=" + ,multiply(x, y))
elif type=="division":
    print("x" ,+"/"+ ,"y" + ,divide(x, y))

else:
    print("Enter division,subtraction,addition,multiplication")


