import json
import time

def load_todos():
    """
    This function loads the To-Do list from the JSON file and returns it.
    If the file does not exist, it returns an empty list.

    Returns:
        list: The To-Do list
    """
    try:
        with open('to_do.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"❌ An error occurred while loading todos: {e}")
        return [] # return an empty list if the file does not exist, and the user will be able to add a new todo

def save_todos(todos):
    """
    This function saves the To-Do list to the JSON file.

    Args:
        todos (list): The To-Do list
    """
    try:
        with open('to_do.json', 'w') as file:
            json.dump(todos, file, indent=2)
    except Exception as e:
        print(f"❌ An error occurred while saving todos: {e}")

def add_todo():
    """
    This function adds a new To-Do item to the list and saves it to the JSON file.

    Returns:
        None
    """
    todo_item_title = input("Enter the To-Do item title: ")
    todo_item_status = input("Enter the status of the To-Do item (DONE/NOT DONE): ").upper()

    if todo_item_status not in ['DONE', 'NOT DONE']:
        print("⚠️ Invalid status. Setting to 'NOT DONE' by default.")
        todo_item_status = 'NOT DONE'
    
    todo_item_time = time.strftime("%Y-%m-%d %H:%M:%S")
    todos = load_todos()
    todos.append({"title": todo_item_title, "time": todo_item_time, "done": todo_item_status})
    save_todos(todos)
    print("✅ To-Do item added successfully!")

def display_todos():
    """
    This function displays the To-Do list.
    """
    todos = load_todos()
    if not todos:
        print("📭 Your To-Do list is empty.")
    else:
        for i, todo in enumerate(todos, 1):
            print(f"{i}- {todo['title']} - {todo['time']} - {todo['done']}")

def mark_as_done():
    """
    This function marks a task as done by the user.
    """
    todos = load_todos()
    if not todos:
        print("📭 Your To-Do list is empty.")
        return
    
    display_todos()
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["done"] = "DONE"
            save_todos(todos)
            print("✅ Task marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def search_todos():
    """
    This function searches for a task in the To-Do list by title.
    """
    search_title = input("Enter the title to search for: ")
    todos = load_todos()
    found = False
    for todo in todos:
        if search_title.lower() in todo['title'].lower():
            print(f"🔍 {todo['title']} - {todo['time']} - {todo['done']}")
            found = True
    if not found:
        print("❌ No matching tasks found.")

def choice_checker(choice):
    """
    This function checks if the user input is 'exit' and if it is, it prints a message and returns True.
    Otherwise, it returns False.

    Args:
        choice (str): user input

    Returns:
        bool: True if the user input is 'exit', False otherwise
    """
    if choice.lower() == 'exit':
        print("👋 Thank you for using the To-Do program, come back again soon!")
        return True
    return False

def start_todo():
    while True:
        print("\n1. Add a new To-Do item")
        print("2. Display To-Do list")
        print("3. Mark a task as done")
        print("4. Search tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice_checker(choice):
            break
        
        if choice == '1':
            add_todo()
        elif choice == '2':
            display_todos()
        elif choice == '3':
            mark_as_done()
        elif choice == '4':
            search_todos()
        elif choice == '5':
            print("👋 Thank you for using the To-Do program, come back again soon!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


start_todo()