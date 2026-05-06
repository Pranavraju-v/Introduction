x=10
for i in range(x):
    if i%20==0:
        print("twist")
    elif i%15==0:
        pass
    elif i%5==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    else:
        print(i)