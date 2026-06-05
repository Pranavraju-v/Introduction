tupel=(1, 0, 1, 1, 1, 0, 1)
rain=0
sun=0

for i in range(1,7):
    if tupel==0:
        rain=rain+1
    else:
        sun=sun+1
if sun<rain:
    print("Bad weather")
else:
    print("Good weather")
