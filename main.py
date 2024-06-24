from filesProcess import readFile, writeToFile

while True:
    answer = input("Do you want to add a new To-Do item [Y or N]?")
    if answer == "exit":
        print("Thank you for using the To-Do program, please, come back again soon.")
        break
    elif answer.upper() == "Y":
        content = input("Please type in your new To-Do item: ")
        writeToFile(content + " ")
    elif answer.upper() == "N":
        answer = input("Do you want to list your To-Do items [Y or N]?")
        if answer.upper() == "Y":
            readFile()
        elif answer.upper() == "N":
            continue
