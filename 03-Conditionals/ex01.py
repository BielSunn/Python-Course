# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    extra_hours = hours - 40
    hours = 40 + (extra_hours * 1.5)


print(f'Pay: {hours * rate}')
