

print("=== Welcom to To-Do List program ====")
user_input=input("do you want to add a new To-Do item? enter(y) for yes and (n) for no : ")

while user_input != "exit" :
   if user_input.lower() == "y":
      print("----------------------------")
      user_note=input("type your note to be saved in your new To-Do item  : ")
      file=open("to_do.txt","a+",encoding="UTF-8")
      file.write(user_note+"\n")
      file.close()
   elif user_input.lower()=="n":
      print("----------------------------")
      
      user_second_input=input("do you want to list your To-Do items ?answer (y) for yes and (n) for no: ")
      if user_second_input =="y":
         file=open("to_do.txt","r",encoding="UTF-8")
         file.seek(0)
         file_list=file.readlines()
         for i in file_list:
            print(i)
         file.close()
      if user_second_input =="n":
         break
   else:
      print("incorrect input ")
   user_input=input("do you want to add a new To-Do item? enter(y) for yes and (n) for no : ")
 

print("=== Thank you for using the To-Do program, come back again soon ===")



   