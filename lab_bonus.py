
import json
from datetime import date

today = date.today()
print("Today's date:", today)


 
user_input_task = input("Please Type your items/tasks :  ")
user_input_date = input("Please Type the date:  ")
user_input_done = input("is it done?? :  ")



# Data to be written
dictionary = {
    "title": user_input_task,
    "date": user_input_date,
    "done": user_input_done,
    
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=2)
 
# Writing to sample.json
with open("lab_json.json", "w") as outfile:
    outfile.write(json_object)
print("JSON file created successfully...")
print(json_object)


for i in json_object:
    print(json_object)
