from datetime import datetime
import json
import os

def readFile():
    if os.stat("toDoItems.txt").st_size != 0:
        # Opening JSON file
        file = open("toDoItems.txt", "r", encoding = "UTF-8")
        # returns JSON object as a dictionary
        try:
            toDos = json.load(file)
        except Exception as e:
            print(e)
        file.close()
    else:
        raise Exception("toDo file is empty!")

    return toDos


def writeToFile(toDo):
    # convert into JSON:
    jsonToDo = json.dumps(toDo)
    #the result is a JSON string:
    file = open("toDoItems.txt", "w")
    file.write(jsonToDo)
    file.close()

