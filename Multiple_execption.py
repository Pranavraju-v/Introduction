try:
    num1, num2=eval(input("Enter 2 numers speperated by commas: "))
    result=num1/num2
    print("Result is ", result)
except ZeroDivisionError:
    print("Division by 0is error")
except SyntaxError:
    print("Enter nuber sperarted by comma like this 1, 2")
else:
    print("No error")
finally:
    print("This will print no matter what")
 