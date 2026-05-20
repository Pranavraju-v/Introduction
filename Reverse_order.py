number = int(input())

count = 0

if number == 0:
    count = 1
else:
    if number < 0:
        number = -number
        
    while number > 0:
        count = count + 1
        number = number // 10

print(count)