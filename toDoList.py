def readFile():
    file = open("to_do.txt", "r", encoding = "UTF-8")
    file.seek(0)
    content = file.read()
    items = content.split(" ")
    print("Your items in To Do List are:")
    for item in items:
        print(item)
    file.close()


def writeToFile(content):
    file = open("to_do.txt", "a+", encoding = "UTF-8")
    file.write(content)
    file.close()

