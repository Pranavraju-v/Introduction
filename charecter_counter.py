string=input("Enter your word: ")
char=input("Enter the charecter of your wish: ")
i=0
count=0
while (i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1
print("the word", string ,"has", count , char,"s")