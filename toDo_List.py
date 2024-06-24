def todo_program():
    while True:
        user_input = input("Do you want to add a new To-Do item? Answer 'y' for yes and 'n' for no (or type 'exit' to quit): ")
        
        if user_input == 'exit':
            print("Thank you for using the To-Do program, come back again soon!")
            break
        elif user_input == 'y':
            todo_item = input("Please type in your new To-Do item: ")
            with open("to_do.txt", "a") as file:
                file.write(todo_item + "\n")
        elif user_input == 'n':
            read_input = input("Do you want to list your To-Do items? Answer 'y' for yes and 'n' for no: ")
            if read_input == 'y':
                try:
                    with open("to_do.txt", "r") as file:
                        todos = file.readlines()
                        print("Your To-Do items are:")
                        for item in todos:
                            print(item.strip())
                except FileNotFoundError:
                    print("You have no To-Do items yet.")
            elif read_input == 'n':
                continue
            else:
                print("Invalid input. Please type 'y' or 'n'.")
        else:
            print("Invalid input. Please type 'y' or 'n'.")

todo_program()
