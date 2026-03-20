a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print("The id of a",id (a))
print("the id of b",id (b))
print("the id of c",id (c))

print(a is b)
print(b is c)
print(a is c)
print(a is not b)
print(b is not c)
print(a is not c)