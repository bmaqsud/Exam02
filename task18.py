numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
kvadrat=[{'value': i['value']**2} for i in numbers]

print(kvadrat)