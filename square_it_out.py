input=input("Enter the range seperated by commas like so 1, 2, 3, 4: ")
list=input.split(",")
square_value=[]
even_list=[]
odd_list=[]
for num in list:
    squered_num=int(num)**2
    square_value.append(squered_num)
    if squered_num//2==0:
        even_list.append(squered_num)
    else:
        odd_list.append(squered_num)
print(square_value)
print("odd list", even_list)
print("even list", odd_list)