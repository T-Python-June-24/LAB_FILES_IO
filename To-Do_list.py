file=open("To_Do_List.txt" , "a+" , encoding="UTF-8")
while True:
    User_question=input("Want to add a new to-do item?answer 'y' for yes and 'n' for no. : ")
    if User_question == "y":
        To_do_y=input("Writing a new to-do item:")
        file.write(f"{To_do_y}\n")
    elif User_question == "n":
        To_do_n=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no. : ")
        if To_do_n == "y":
            file.seek(0)
            print(file.read())
    elif User_question == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
        
            