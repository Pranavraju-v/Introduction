import random
playing=True
rand=str(random.randint(0,9))
print("Guess any singel digit number right and you win ")
print(rand)

while playing:
    guess=input("Enter the number:  ")
    if guess==rand:
        print("You win")
        break
    else:
        print("Your guess was wrong try again") 