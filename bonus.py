import json

file=open("To_Do_List.json" , "a+" , encoding="UTF-8")
try:
    file.seek(0)
    tasks = json.load(file)
except json.JSONDecodeError:
    task = []
task = []
while True:
    User_question=input("Want to add a new to-do item?answer 'y' for yes and 'n' for no. : ")
    if User_question.lower() == "y":
        while True:
            print("Enter tasks:-")
            title= input("title : ")
            date_tome=input("date & time( dd-mm-yy hh-mm-ss) : ")
            task1={"title": title , "date & time":date_tome , "done":False}
            task.append(task1)
            write = json.dumps(task, ensure_ascii=False, indent=4)
            file.seek(0)
            file.write(write)
            file.truncate()
            exit=input("Do you want to Exit ? answer 'y' for yes and 'n' for no. : ")
            if exit.lower() == "y":
                break
    elif User_question.lower() == "n":
        To_do_n=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no. : ")
        if To_do_n.lower() == "y":
            file.seek(0)
            tasks=json.loads(file.read())
            for num , key in enumerate(tasks , 1):
                print(f"{num} - {key['title']} - {key['date & time']} - {'done' if key['done'] else 'not done'}")
    elif User_question.lower() == "exit":
        print("thank you for using the To-Do program, come back again soon")
        file.close()
        break