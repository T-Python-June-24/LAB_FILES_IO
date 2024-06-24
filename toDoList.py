def readFile():
    file = open("to_do.txt", "r", encoding = "UTF-8")
    file.seek(0)
    content = file.read()
    print(content)
    file.close()


def writeToFile(content):
    file = open("to_do.txt", "a+", encoding = "UTF-8")
    file.write(content + "\n")
    file.close()

