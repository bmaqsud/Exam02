import json
with open("input/students.json", 'r') as file:
    students=json.load(file)
ismlari=[student['name'] for student in students]
ismlari.sort()


with open('Output/output12.txt', 'w') as file:
    for ism in ismlari:
        file.write(ism + '\n')