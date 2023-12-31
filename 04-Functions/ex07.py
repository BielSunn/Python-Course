'''
Exercise 7: Rewrite the grade program from the previous chapter using a
function called computegrade that takes a score as its parameter and returns a grade as a string.
'''


def computegrade(score):
    if score < 0 or score > 1:
        grade = "Bad score"
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8 and score < 0.9:
        grade = "B"
    elif score >= 0.7 and score < 0.8:
        grade = "C"
    elif score >= 0.6 and score < 0.7:
        grade = "D"
    else:
        grade = "F"
    return grade


try:
    score = float(input("Enter score: "))
    grade = computegrade(score)
    print(grade)
except:
    print("Bad score")
    quit()
