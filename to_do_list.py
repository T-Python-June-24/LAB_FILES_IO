# The same solution without using "exit"
'''
def prompt(prompt:str) -> bool:
    while True:
        choice = input(prompt + " [y/n] ")
        if choice.lower()  == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Incorrect input")

while True:
    if prompt("Do you want to add a new To-Do item?"):
        file = open("To_Do.txt", "a+", encoding="utf-8")
        file.write(input("Type your new To-Do item: ") + "\n")
        file.close()
    else:
        if prompt("Do you want to list your To-Do items?"):
            file = open("To_Do.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
        else:
            break
'''

while True:
    user_input = input("Do you want to add a new To-Do item? [y/n] ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "y":
        file = open("To_Do.txt", "a+", encoding="utf-8")
        file.write(input("Type your new To-Do item: ") + "\n")
        file.close()
    elif user_input.lower() == "n":
        user_input = input("Do you want to list your To-Do items? [y/n] ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "y":
            file = open("To_Do.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
        else:
            continue
    else:
        print("Incorrect input.")
print("Thank you for using the To-Do program, come back again soon")