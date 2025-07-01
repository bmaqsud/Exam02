students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]

qisqa_ism=min(students, key=lambda i: len(i['name']))['name']

print(f"eng qisqa ism: {qisqa_ism}")