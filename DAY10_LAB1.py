
# # LAB_FILES_IO


# ## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
# - Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
# - If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
# - If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
# - If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
# - Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"


def add_todo():
    todo = input("Enter your new To-Do: ").strip()

    file = open("to_do.txt", "a+")
    file.write(todo + "\n")
    file.close()

    print("To-Do added successfully")



def list_todo():
        file = open("to_do.txt", "r")
        todo = file.readlines()
        file.close()

        if todo:
            print("Your To-Do list:")

            for idx, item in enumerate(todo, 1):
                print(f"{idx}. {item.strip()}")

        else:
            print("Your To-Do list is empty")




#####################

def main():
    while True:

        action = input("Do you want to add a new To-Do item? (y/n or type 'exit' to exit): ")

        if action.lower() == "y":
            add_todo()

        elif action.lower() == "n":

            list_action = input("Do you want to list your To-Do? (y/n): ")

            if list_action.lower() == "y":
                list_todo()
            elif list_action.lower() == "n":
                continue
            else:
                print("Invalid input. Please enter 'y' or 'n'")


        elif action.lower() == "exit":
            print("Thank you!")
            break


        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'")


main()
