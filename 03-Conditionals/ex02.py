# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

    if hours > 40:
        extra_hours = hours - 40
        hours = 40 + (extra_hours * 1.5)

    print(f'Pay: {hours * rate}')

