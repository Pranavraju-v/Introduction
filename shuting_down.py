def shutdown(user_input):
    if user_input=="yes":
        return("Shuting down")
    elif user_input=="no":
        return("Abort shutdown")
    else:
        return("Sorry")
user_input=input("turn off computer?: ")
print(shutdown(user_input))