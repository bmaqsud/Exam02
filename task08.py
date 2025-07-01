with open('Input/numbers.txt', 'r' ) as file:
    sonlar=file.readlines()
 

total=0
for son in sonlar:
    total+=int(son)


with open('Output/output08.txt', 'w') as file:
    file.write(str(total))