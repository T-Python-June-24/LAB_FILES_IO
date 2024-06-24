while True:
    user_choice = input("Do you want to add a new To-Do item? (y/n): ").lower()
    if user_choice == 'exit':
        print("Thank you for using the To-Do program, come back again soon!")
        break
    
    if user_choice == 'y':
        todo_item = input("Enter the To-Do item: ")
        if todo_item == 'exit':
            print("Thank you for using the To-Do program, come back again soon!")
            break
        with open('to_do.txt', 'a') as file:
            file.write(todo_item + '\n')
        print("To-Do item added successfully!")
        
    elif user_choice == 'n':
        list_ask = input("View To-Do list? (y/n): ").lower()
        if list_ask == 'exit':
            print("Thank you for using the To-Do program, come back again soon!")
            break
        if list_ask == 'y':
            try:
                with open('to_do.txt', 'r') as file:
                    todo_list = file.read()
                    if todo_list:
                        print("Your To-Do List:")
                        print(todo_list)
                    else:
                        print("Your To-Do list is empty.")
            except FileNotFoundError:
                print("No To-Do list found. Add some items first!")
                
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

