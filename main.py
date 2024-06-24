file = open('to_do.txt', "a+")

while True:

    x = input("do yo want to enter something to your to do list? 'Y' for yes 'N' for no and 'exit' to exit the program: ")

    if x.upper() == "EXIT":
        print("Thank you for being here")
        break

    elif x.upper() == "Y":
        ToDo = input("Add an Activity to your to do list: ")
        Time1 = input(f"Add the time to {ToDo}: ")
        Date1 = input(f"Also the date to {ToDo}: ")
        file.write(f"On {Date1} at {Time1} you will be {ToDo} \n")


    elif x.upper() == "N":

        y=input("Do you want to check your TO DO list, 'Y' for Yes and 'N' for No or 'exit' to exit the program: ")

        if y == "exit":
            print("See ya next time")

        elif y.upper() == "Y":
            file.seek() 
            tasks = file.readlines()

            if tasks:
                print("Your To-Do List:")
                for t in tasks:
                    print(t)

            else:
                print("Your To-Do list is currently empty.")

        elif y.upper() == "N":
            print("see ya")

    else:
        print("That's an invalid input")

file.close()