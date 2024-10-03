hours_worked = int(input("Enter hours worked : "))
pay_rate = 3
if hours_worked <=40:
    gross_pay = pay_rate * hours_worked

else:
    basic_pay = pay_rate * 40
    overtime = hours_worked -40
    overtime_pay = 1.5* pay_rate * overtime
    gross_pay =basic_pay + overtime_pay

print(gross_pay)
