amount=int(input("Type the amount of your wish:"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print(note1,"100 notes")
print(note2,"50 notes")
print(note3,"10 notes")