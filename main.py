
while True:
  add_list_item = str(input("do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no. "))
  if add_list_item == "exit":
    print("thank you for using the To-Do program, come back again soon")
    break
  elif add_list_item == "y":
    todo_item = str(input("Type your new To-Do item: "))
    file = open("to_do.txt", "a", encoding="utf-8")
    file.write(todo_item + "\n")
    file.close()
  elif add_list_item == "n":
    read_todo = str(input("Do you want to list your To-Do items? answer \"y\" for yes and \"n\" for no. "))
    if read_todo == "y":
      file = open("to_do.txt", "r", encoding="utf-8")
      file_content = file.read()
      print(file_content)
      file.close()
