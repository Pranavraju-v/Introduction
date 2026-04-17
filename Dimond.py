row_num=5
space=row_num-1
for i in range(1, row_num+1):
    for j in range(1, space+1):
        print(end=" ")
    space=space-1
    for j in range(2*i-1):
        print(end="*")
    print()

space=1
for i in range(1, row_num):
    for j in range(1, space+1):
        print(end=" ")
    space=space+1
    for j in range(1, 2*(row_num-i)):
        print(end="*")
    print()