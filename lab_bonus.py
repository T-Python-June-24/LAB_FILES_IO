import json
import datetime


def load_tasks():
    with open("lab_json.json", "r") as infile:
         tasks = json.load(infile)
    if not isinstance(tasks, list):
                tasks = []
    return tasks

def save_tasks(tasks):
    with open("lab_json.json", "w") as outfile:
        json.dump(tasks, outfile, indent=2)

def add_task():
    tasks = load_tasks()

    user_input_task = input("Please Type your items/tasks: ")
    user_input_date = input("Please Type the date and time (YYYY-MM-DD HH:MM:SS): ")
    user_input_done = input("Is it done?? (yes/no): ").lower()

    new_task = {
        "title": user_input_task,
        "date": user_input_date,
        "done": user_input_done == 'yes'
    }

    tasks.append(new_task)
    save_tasks(tasks)
    
    print("Task added successfully...")
    print(json.dumps(new_task, indent=2))
    return new_task

def display_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['date']} - {status}")


while True:
    user_input = input("\n\nPress 1 to add items ✅\t\tPress 2 to Display Tasks 📝\n\n\nPress 3 to Exit 🚪\n\n").lower()
    if user_input == "1":
        add_task()
    elif user_input == "2":
        print("Here is your Tasks 📝🌎\n")
        display_tasks()
    elif user_input == "3":
        break
    else:
        print("Invalid option. Please try again.")
