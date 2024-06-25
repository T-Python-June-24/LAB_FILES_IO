import json
from datetime import datetime

# قائمة المهام
todo_list = [
    {"title": "Go to Gym", "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "done": False},
    {"title": "Visit Grandma", "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "done": False}
]

# فتح الملف في وضع الكتابة
with open("to_do.json", "w") as file:
    # كتابة البيانات بصيغة JSON في الملف مع تنسيق جميل
    json.dump(todo_list, file, indent=3)
