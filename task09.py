with open('Input/numbers.txt', 'r' ) as file:
    sonlar=file.readlines()


max_son=max(int(son.strip()) for son in sonlar if son.strip().isdigit())


with open('Output/output09.txt', 'w') as file:
    file.write(str(max_son))