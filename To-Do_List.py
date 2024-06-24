while True:
    userInput = input("Do you want ot add a new To-Do item? y or n: ")
    
    if userInput == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break
    elif userInput == "y" :
        toDoInput = input("Please add task: ")
        file = open("to_do.txt", "a+" , encoding="UTF-8")
        file.write(toDoInput + "\n")
        file.close()
        
    elif userInput == "n" :
        noInput = input("Do you want to list your To-Do Items? answer \"y\" for yes and \"n\" for no.")
        if noInput == "y" :
            file = open("to_do.txt", "r" , encoding="UTF-8")
            print(file.read())
            file.close()
        elif noInput == "n" :
            continue
