num1=[1, 2, 3]
num2=[4, 5, 6]
ans=map(lambda x, y:x + y, num1, num2)
print("addition of 2 lists: ")
print((list(ans)))
nums=[1, 2, 3, 4, 5]
def sq(n):
    return n*n
squere=list(map(sq, nums))
print(squere)