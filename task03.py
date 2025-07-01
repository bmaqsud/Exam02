maosh=float(input("maqoshingizni kiritng: "))

def calculate_tax(salary):
    if salary>5_000_000:
        return salary*0.20
    else:
        return salary*0.13
    
def calculate_net_salary(salary):
    return salary-calculate_tax(salary)


soliq=calculate_tax(maosh)
sof_maosh=calculate_net_salary(maosh)
print(f"siz {soliq} to'ladingiz sizning sof foydangiz {sof_maosh}")