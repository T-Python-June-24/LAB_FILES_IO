import json
from datetime import datetime


import json
import os
from datetime import datetime

filename = 'to_do.json'

# Load existing tasks from the JSON file if it exists
if os.path.exists(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        tasks = json.load(file)
else:
    tasks = {}

while True:
    user_input = input("Do you want to add a new To-Do item? (y or n): ").strip().lower()
    
    if user_input == "exit":
        print("Thank you for using the To-Do program. Come back again soon!")
        break
    elif user_input == "y":
        title = input("Please add a task: ").strip()
        task_id = len(tasks) + 1
        tasks[task_id] = {
            "title": title,
            "date & time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "done": False
        }
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(tasks, file, indent=4)
        print(f"Task added and saved to {filename}")
    elif user_input == "n":
        no_input = input('Do you want to list your To-Do Items?  ')
        if no_input == "y":
            if tasks:
                print("Your To-Do List:")
                for task_id, task in tasks.items():
                    status = "DONE" if task["done"] else "NOT DONE"
                    print(f"{task_id}- {task['title']} - {task['date & time']} - {status}")
            else:
                print("Your To-Do list is empty.")
        elif no_input == "n":
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")
