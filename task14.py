import json
with open("input/students.json", "r") as file:
    students=json.load(file)

a_names=[student['name'] for student in students if student['name'].startswith('A')]

natija={'a_names':a_names}

with open("Output/output14.json", "w") as file:
    json.dump(natija, file)