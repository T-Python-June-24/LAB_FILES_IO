import json

file = open("To_Do_List.json", "r+", encoding="UTF-8")

try:
    file.seek(0)
    tasks = json.load(file)
except json.JSONDecodeError:
    tasks = []

while True:
    User_question = input("Want to add a new to-do item? Answer 'y' for yes and 'n' for no. : ")
    if User_question.lower() == "y":
        while True:
            print("Enter tasks:-")
            title = input("title: ")
            date_time = input("date & time (dd-mm-yy hh-mm-ss): ")
            task = {"title": title, "date & time": date_time, "done": False}
            tasks.append(task)
            write = json.dumps(tasks, ensure_ascii=False, indent=4)
            file.seek(0)
            file.write(write)
            file.truncate()
            exit_input = input("Do you want to Exit? Answer 'y' for yes and 'n' for no. : ")
            if exit_input.lower() == "y":
                break
    elif User_question.lower() == "n":
        To_do_n = input("Do you want to list your To-Do items? Answer 'y' for yes and 'n' for no. : ")
        if To_do_n.lower() == "y":
            file.seek(0)
            tasks = json.load(file)
            for num, task in enumerate(tasks, 1):
                print(f"{num} - {task['title']} - {task['date & time']} - {'Done' if task['done'] else 'Not Done'}")
    elif User_question.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        file.close()
        break
