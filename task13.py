import json

with open("input/students.json", "r") as file:
    students=json.load(file)

long_names=[student['name'] for student in students if len(student['name']) > 5]

natija={'long_names':long_names}

with open("Output/output13.json", "w") as file:
    json.dump(natija, file)