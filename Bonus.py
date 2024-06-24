import json
from datetime import datetime

def loading(fjson="To-Do.json"):
    try:
        with open(fjson, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saving(todos, fjson="To-Do.json"):
    with open(fjson, "w", encoding="UTF-8") as file:
        json.dump(todos, file, indent=4)

def add_todo():
    title = input("Type in your new To-Do item: ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    done = False
    todo = {"title": title, "date_time": date_time, "done": done}
    todos.append(todo)
    saving(todos)
    print("To-Do item added.")

def list_todos():
    if todos:
        print("\n-------- TO DO LIST --------")
        for i, todo in enumerate(todos, 1):
            status = "DONE" if todo["done"] else "NOT DONE"
            print(f"{i}- {todo['title']} - {todo['date_time']} - {status}")
        print("----------------------------")
    else:
        print("Your to-do list is empty.")

def mark_done():
    list_todos()
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["done"] = True
            saving(todos)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def search_todos():
    search_title = input("Enter the title to search: ").lower()
    results = [todo for todo in todos if search_title in todo["title"].lower()]
    if results:
        print("\n-------- SEARCH RESULTS --------")
        for i, todo in enumerate(results, 1):
            status = "DONE" if todo["done"] else "NOT DONE"
            print(f"{i}- {todo['title']} - {todo['date_time']} - {status}")
        print("----------------------------")
    else:
        print("No tasks found with that title.")

def show_menu():
    print("\n-------- TO DO MENU --------")
    print("1. Add a new To-Do item")
    print("2. List all To-Do items")
    print("3. Mark a To-Do item as done")
    print("4. Search To-Do items by title")
    print("5. Exit")
    print("----------------------------")

todos = loading()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_todo()
    elif choice == '2':
        list_todos()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        search_todos()
    elif choice == '5':
        print("Thank you for using the To-Do program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")