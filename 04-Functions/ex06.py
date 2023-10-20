'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate).
'''


def computepay(hours, rate):
    if hours > 40:
        extra_hours = hours - 40
        hours = 40 + (extra_hours * 1.5)
    pay = hours * rate
    return pay


try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hours, rate)
    print(f'Pay: {pay}')
except:
    print("Error, please enter numeric input")
    quit()
