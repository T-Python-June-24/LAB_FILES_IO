import os ,json
from datetime import datetime
 
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def saveInJson(toDoList):
    with open("ToDoList.json", "w") as file:
        json.dump(toDoList, file, indent=4)

def addToDoItem(toDoList):
    title = input("Please enter your new To-Do item: ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    toDoList.append({"Title": title, "DateTime": date_time, "Done": False})
    saveInJson(toDoList)

def loadFromJosn():
    try:
        with open("ToDoList.json", "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        print("\033[31m Error",e,"\033[34m")
        return []

def displyToDoItems(toDoList):
    if toDoList:
        print("\nYour To-Do items: \n ")
        for i, item in enumerate(toDoList, start=0):
            status = "Done" if item["Done"] else "Not Done"
            print(f"{i}. {item['Title']} - {item['DateTime']} - {status}")
    else:
        print("\n\033[31m Your To-Do list is empty.\033[34m\n")

def SetItemDone(toDoList):
    if toDoList:
        displyToDoItems(toDoList)
        index = input("Please enter the number of the task you want to set as done: ")
        if not index.isnumeric():
            print("\n\033[31m You enterd ab invalid number \033[34m\n")

        else:
            index = int(index)
            if index < len(toDoList):
                toDoList[index]["Done"] = True
                saveInJson(toDoList)
            else:
                    print("\n\033[31m You enterd ab invalid number \033[34m\n")
                    SetItemDone(toDoList)
    else:
        print("\033[31m Your To-Do list is empty.\033[34m")


def SearchToDoItems(toDoList):
    if toDoList:
        try:    
            search_term = input("Enter the title to search for: ").lower()
            results = [item for item in toDoList if search_term in item["Title"].lower()]
            if  results:
                print("\n\033[32m Search results: \033[34m\n")
                for item in results:
                    status = "DONE" if item["Done"] else "NOT DONE"
                    print(f"\n\033[32m {item['Title']} - {item['DateTime']} - {status} \033[34m\n")
            else:
                print("\n\033[31m No matching tasks found.\033[34m")
        except Exception as e :
            print(f"\n\033[31mError: {e} \033[34m")
    else:
        print("\n\033[31m Your To-Do list is empty.\033[34m")


def main():

    toDoList = loadFromJosn()

    while(True):
        clearTerminal()
        print(f''' \033[36m 
    ---------------------------------------------    
        Welcome in To-Do List app 🗓️ ✅                   
    ---------------------------------------------    
        \033[34m1- Add new To-Do item 📥
              
        2- View To-do list 🗓️
            
        3- Set a task to done ✅
              
        4- Search To-Do items by title 🗓️
        
        5- Exit 👋
              ''')

        userInput = input("Enter a number from the above menu: ")

        if userInput == "1" :
                addToDoItem(toDoList)
                while True:           
                    userInput = input("Enter 5 to exit and 1 to add another to-do: ")
                    if userInput == "5":
                        break
                    elif userInput == "1":
                        addToDoItem(toDoList)
                    else:
                        print(f"\033[31mError: you enterd invalid number\033[34m")
        
        elif userInput == "2":

            displyToDoItems(toDoList)
                
            input("Press enter to continue..")
                
        
        elif userInput == "3": 

            SetItemDone(toDoList)
            input("Press enter to continue..")
        
        elif userInput == "4": 

            SearchToDoItems(toDoList)
            input("Press enter to continue..")
        
        elif userInput == "5": 
            print(f'''\033[33m 
                
                Thank you for using the To-Do program, come back again soon 👋

                ''')
            break
        else :

            print(f'''\033[31m 
        
        Error: You enterd invalid number please enter only 1 or 2 or 3 or 4 or 5
        \033[34m''')
            input("Press enter to continue..")


try:

    main()

except Exception as e :

    print(f'''\033[31m 
        
        Error: {e}
        \033[34m''')
