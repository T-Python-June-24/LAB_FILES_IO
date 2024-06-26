
# # Bonus
# ## Modify the project to be able to do the following instead of  writing the to do items line by line (**hint**: use the `json` module):
# - each to-do item should be saved with the following attributes:
# - - title
#   - date & time
#   - done (default is false)

# - User can display his to do list items as follows:
#   ```
#   1- Go to Gym - 2023-08-05 08:00:00 - DONE
#   2- Visit Grandma - 2023-08-08 21:00:00 - NOT DONE
#   ```
# - User can mark a specific Task as Done.
# - User can search in his tasks using the title.




import json
from datetime import datetime



TODO_FILE = "to_do.json"



def load_todo():
    file = open(TODO_FILE, "r")
    todo = json.load(file)
    file.close()
    return todo



def save_todo(todo):
    file = open(TODO_FILE, "w")
    json.dump(todo, file, indent= 4)
    file.close()



def add_todo():
    title = input("Enter your new To-Do title: ").strip()
    date_time_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date and time format")
        return
    
    todo = {
        "title": title,
        "date_time": date_time_str,
        "done": False
    }
    
    todo_list = load_todo()
    todo_list.append(todo)
    save_todo(todo_list)
    print("To-Do added successfully")




def list_todo():
    todo = load_todo()
    if todo:
        print("Your To-Do list:")

        for i, item in enumerate(todo, 1):
            status = "DONE" if item["done"] else "NOT DONE"

            print(f"{i}- {item['title']} - {item['date_time']} - {status}")
    else:
        print("Your To-Do list is empty")




def mark_as_done():
    pass




def search_by_title():
    pass








def main():
    while True:

        action = input("Do you want to add a new To-Do? (y/n or type 'exit' to quit): ")

        if action.lower() == "y":
            add_todo()

        elif action.lower() == "n":
            list_action = input("Do you want to list your To-Do? (y/n): ") #or type 'mark' to mark as done, 'search' to search by title): ")
            if list_action.lower() == "y":
                list_todo()
            elif list_action.lower() == "n":
                continue
            else:
                print("Invalid input. Please enter 'y' or 'n' ")

        elif action.lower() == "exit":
            print("Thank you!")
            break

        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")



main()
