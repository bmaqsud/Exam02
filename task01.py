son1=int(input("sonni kiriting: "))
amal=input("(+), (-), (*), (/) kabi ammalardan birini kiriting: ")
son2=int(input("sonni kiriting: "))

def add(son1, son2):
    return son1+son2

def substract(son1, son2):
    return son1-son2


def multiply(son1, son2):
    return son1*son2

def devide(son1, son2):
    if son2!=0:
        return son1/son2
    else:
        print("nolga bo'lib bo'lmaydi!")


if amal=='+':
    print(add(son1, son2))

if amal=='-':
    print(substract(son1, son2))

if amal=='*':
    print(multiply(son1, son2))

if amal=='/':
    print(devide(son1, son2) )   