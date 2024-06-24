file1 = open("To-Do.txt", "a+", encoding="UTF-8")

while True:
    answ1= input("Do you want to add a new To-Do item? ('y' or 'n'): ")
    if answ1 == 'y':
        item = input("type in your new To-Do item: ")
        file1.write(item+"\n")
        file1.close()
    elif answ1 == 'n':
        answ2= input("Do you want to list your To-Do items? ('y' or 'n'): ")
        if answ2 == 'y':
            print("\n-------- TO DO LIST --------")
            file = open("To-Do.txt", "r", encoding="UTF-8")
            content = file.read()
            print(content)
            file.close()
            print("----------------------------")
            continue
        else:
            answ1 = "exit"
    if answ1 == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break