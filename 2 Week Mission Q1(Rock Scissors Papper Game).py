
user = "가위 바위 보 게임에 오신걸 환영합니다."
print(user)

# 가위 바위 보의 입력 값을 정수 형태로 변환
def getUserInput(a):
    while True : # while을 통해 입력값이 제대로 될때까지 반복
        a = input("가위 바위 보:")
        if a == "" :
            print("가위 바위 보를 입력하세요.")
            continue
        elif a == "가위" :
            user = int(0)
        elif a == "바위":
            user = int(1)
        elif a == "보":
            user = int(2)
        else :
            print("가위 바위 보를 입력하세요.")
            continue
        break
    return user

def game(u, c) :
    result = "결과"
    if u == c :
        result = "비겼습니다!"
    elif u == 0 and c == 1 :
        result = "컴퓨터 승리!" # u-c = -1
    elif u == 0 and c == 2 :
        result = "유저 승리!" # u-c = -2
    elif u == 1 and c == 2 :
        result = "컴퓨터 승리!" # u-c = -1
    elif u == 1 and c == 0 :
        result = "유저 승리!" # u-c = 1
    elif u == 2 and c == 0 :
        result = "컴퓨터 승리!" # u-c = 2
    elif u == 2 and c == 1 :
        result = "유저 승리!" # u-c = 1
    else :
        print("Error1")

    # 연산을 이용한 결과출력 방법
    # result = u - c
    # if result == 0
    #     result = "비겼습니다!"
    # elif result == -1 or 2
    #     result = "컴퓨터 승리!"
    # elif result == -2 or 1
    #     result = "유저 승리!"
    # else :
    #     print("Error1")
    return result

# 정수 값을 가위 바위 보로 변환
def getResult (val) :
    r = "결과"
    if val == 0:
        r = "가위"
    elif val == 1:
        r = "바위"
    elif val == 2:
        r = "보"
    else:
        print("Error2")
    return r



while True :
    u = getUserInput(user)
    # print(u)

    import random

    computer = random.randint(0, 2)
    c = int(computer)
    # print(c)

    gr = game(u, c)
    print("유저 =", getResult(u))
    print("컴퓨터 =", getResult(c))
    print(gr)
    if gr == "유저 승리!" :
        break
    else :
        continue
