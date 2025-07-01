with open('Input/numbers.txt', 'r' ) as file:
    sonlar=[int(i.strip()) for i in file]


sonlar.sort()


with open('Output/output10.txt', 'w') as file:
    for son in sonlar:
        file.write(str(son) + '\n')