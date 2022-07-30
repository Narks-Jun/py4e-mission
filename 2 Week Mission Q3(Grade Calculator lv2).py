name = input("당신의 이름은?")
score = input("당신의 점수는?")
try :
    sc = int(score)
except :
    print("Error, Please Input Your Scroe")
    quit()

def grade(x, y) :
    if sc >= 95 :
        grade = "A+"
    elif score >= 90 :
        grade = "A"
    elif score >= 85 :
        grade = "B+"
    elif score >= 80 :
        grade = "B"
    elif score >= 75 :
        grade = "C+"
    elif score >= 70 :
        grade = "C"
    elif score >= 65 :
        grade = "D+"
    elif score >= 60 :
        grade = "D"
    elif score < 60 :
        grade = "F"
    else :
        grade = "없음"
    return grade
g = grade(name,score)
print("학생이름:",name)
print("점수:", score)
print("학점:",g)
