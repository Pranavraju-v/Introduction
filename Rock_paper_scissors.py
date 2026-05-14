import random

while True:
    user_input=str(input("Enter choice(rock,paper,scissors): "))
    possible=["rock","paper","scissors"]
    computer_input=random.choice(possible)
    print("You chose:",user_input,"computer chose:",computer_input)

    
    if user_input==computer_input:
        print("draw")
    elif user_input=="rock" and computer_input=="paper": 
        print("The computer wins")
    elif user_input=="paper" and computer_input=="rock":
        print("You win")
    elif user_input=="paper" and computer_input=="scissors":
        print("Computer wins")
    elif user_input=="scissors" and computer_input=="paper": 
        print("you win")
    elif user_input=="rock" and computer_input=="scissors":
        print("You win")
    elif user_input=="scissors" and computer_input=="rock":
        print("computer wins")
