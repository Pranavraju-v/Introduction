students_names={"lisa":89, "Max":79, "Dennis":93, "Pranav":91, "Maria":96}

choice=input("enter the name of the person: ")
print(students_names.get(choice))
print(max(students_names), "Scored the highest")
print(min(students_names), "scored the lowest")
