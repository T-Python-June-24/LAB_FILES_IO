from datetime import datetime
from filesManaging import readFile, writeToFile
import os

def addToDo():
    title = input("Please type in your new To-Do item: ")
    if os.stat("toDoItems.txt").st_size != 0 :
        toDo = readFile()
        toDo[title] = {"date&Time": f"{datetime.now().replace(microsecond=0)}", "done": False}
        writeToFile(toDo)
    else:
        toDo = {}
        toDo[title] = {"date&Time": f"{datetime.now().replace(microsecond=0)}", "done": False}
        print(f"{title} has been added to To-Do list.")
        writeToFile(toDo)



def displayToDos():
    try:
        print("Your To-Do items are:")
        toDos = readFile()
        for index, (title, toDo) in enumerate(toDos.items(),start = 1):
            status = "DONE" if toDo["done"] == True else "NOT DONE"
            dateTime = toDo["date&Time"]
            print(f"{index} - {title} - {dateTime} - {status}")
    except Exception as e:
        print(e)

def markDone():
    title = input("Please type in your To-Do item to mark it DONE: ")
    if os.stat("toDoItems.txt").st_size != 0 :
        toDo = readFile()
        toDo[title]["done"] = True
        writeToFile(toDo)
        print(f"{title} task is DONE!")
    else:
         print("No To-Dos available!")


def findToDo():
    item = input("Please type in your To-Do title to look it up: ")
    if os.stat("toDoItems.txt").st_size != 0 :
        toDo = readFile()
        if item in toDo:
            status = "DONE" if toDo[item]["done"] == True else "NOT DONE"
            dateTime = toDo[item]["date&Time"]
            print(f"{item} - {dateTime} - {status} is FOUND!")
        else:
            print(f"The To-Do, {item} is not FOUND!")


while True:
    answer = input("Press A to add a new To-Do itemn= n, D to display all To-Dos, M to mark a To-DO as DONE or S to search for a To-Do: ")
    if answer == "exit":
        print("Thank you for using the To-Do program, please, come back again soon.")
        break
    elif answer.upper() == "A":
        addToDo()
    elif answer.upper() == "D":
        displayToDos()
    elif answer.upper() == "M":
        markDone()
    elif answer.upper() == "F":
        findToDo()
