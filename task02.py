balans=float(input("Balansni kiriting :"))
print("""   ===MENU===
    1.deposite
    2. withdraw
    3.check balance
""")

amal=int(input("Menudagi amallardan birini kiriting: "))


def deposite(miqdor, balans):
    return balans+miqdor

def withdraw(miqdor, balans):
    if balans < miqdor:
        print("mablag' yetarli emas!")
        return balans
    return balans-miqdor

def check_balance(balans):
    return balans

if amal==1:
    miqdor=float(input("Qo'shmoqchi bo'lgan miqdorni kiriting: "))
    balans=deposite(miqdor, balans)
    print(f"sizning balansingizga {miqdor} qo'shilib {balans}   cha bo'ldi ")
if amal==2:
    miqdor=float(input("Miqdorni kiritng : "))
    balans=withdraw(miqdor,balans)
    print(f"siz kartangizdan {miqdor} pul oldingiz sizda {balans} qoldi")

if amal==3:
    print(f"sizning balansizngiz {check_balance(balans)}")
