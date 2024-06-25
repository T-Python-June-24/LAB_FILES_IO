
import json 
 
file = open("To_Do_List.json", "a+", encoding="UTF-8") 
 
while True: 
    User= input("Do you want to add a new To-Do item? (y/n)") 
    if User.lower() == "y": 
        while True: 
            title = input("title: ") 
            date_time = input("date & time (dd-mm-yy hh-mm-ss): ") 
            task = {"txt": title, "date and time": date_time, "done": False} 
            tasks.append(task) 
            write = json.dumps(tasks, ensure_ascii=False, indent=4) 
            file.seek(0) 
            file.write(write) 
            file.truncate() 
            exit_input = input(" you want to exit the program? (y/n): ") 
            if exit_input.lower() == "y": 
                   break 
    elif User.lower() == "n": 
        To_do_n = input("Do you want to list your To-Do items? (y/n): ") 
        if To_do_n.lower() == "y": 
            file.seek(0) 
            tasks = json.load(file) 
            for num, task in enumerate(tasks, 1): 
                print(f"{num} - {task['title']} - {task['date and time']} - {'Done' if task['done'] else 'continue'}") 
    elif User.lower() == "exit": 
        print("Thank you for using the To-Do program, come back again soon") 
        file.close() 
        break