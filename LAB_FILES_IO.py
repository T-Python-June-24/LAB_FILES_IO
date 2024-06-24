def to_do_program():
    while True:
            file = open("to_do.txt", "+a", encoding="UTF-8")
            print("\n Welcome to abdullah to do list 👋:  \n")
            user_input = input("Please Type your items/tasks :  ")
            if user_input == "exit":
                break
            file.write(user_input+ "\n")
            print("your notes abdullah for now is : \n")    
            #3- close the file
            file.close()
    
    
def display_items():
    file = open("to_do.txt.txt", "r", encoding="UTF-8")
    print(file.read())
 

while True:
    user_input = input("\n\n Press y to add items ✅ \t Press n to Exit 🚪  : ")
    user_input.lower()
    if user_input == "y":
        to_do_program()
    if user_input == "n":
        print("Thank you for useing me To Do App 📝🌎")
        display_items()
        break
    if user_input == "exit":
        print("Thank you for useing me To Do App 📝🌎")
        print("thank you for using the To-Do program, come back again soon 👋")
        break

