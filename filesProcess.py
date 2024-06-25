import os
def readFile():
    if os.stat("to_do.txt").st_size != 0:
        file = open("to_do.txt","r", encoding="UTF-8")
        content = file.read()
        print("You have this list to do:")
        print(content)
        file.close()
    else:
        print("No To-Do to display")


def writeToFile(content):
    file = open("to_do.txt", "a+", encoding = "UTF-8")
    file.write(content + "\n")
    file.close()

