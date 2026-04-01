medical=input("Did You have a medical cause Y/N: ")
if medical=="Y":
    print("You are allowed to write the exam")
attendence=int(input("Enter yor attendence percentage: "))
if attendence>=75:
   print("You are allowed to write the exam")
else:
    print("You are not allowed to write the exam")