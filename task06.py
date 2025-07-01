students = {
    'Ali': 5,
    'Vali': 4,
    'Hasan': 5,
    'Husan': 3
}
baho_yigindi=sum(students.values())
baholar_soni=len(students)
ortacha_baho=baho_yigindi/baholar_soni
print(f"o'rtacha baho: {ortacha_baho}")


alochilar=[]
for ism in students:
    if students[ism]>ortacha_baho:
        alochilar.append(ism)
 
print(f"alochilar : {alochilar}")

