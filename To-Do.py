
print("Welcome")

while True:
    user = input("Do you want to add a new To-Do item? (y/n): ")
    
    if user.lower() == "y":
        new_todo = input("Enter your new To-Do item: ")
        with open('to_do.txt', 'a') as file:
            file.write(new_todo + '\n')
        print(f"'{new_todo}' add To-Do List.")
    
    elif user.lower() == 'n':
        list= input("Do you want to list your To-Do items? (y/n): ")
        if list.lower() == 'y':
                with open('to_do.txt', 'r') as file:
                    todo_list = file.readlines()
                    if todo_list:
                        print("Your List:")
                        for item in todo_list:
                            print(item)
                   
    
    exit= input("if you want to exit the program? write exity ")
    if exit.lower() == 'exit':
        break

print("Thank you for using the To-Do program. Come back again soon!")
