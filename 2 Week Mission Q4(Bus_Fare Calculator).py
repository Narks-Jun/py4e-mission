age = input("당신의 나이는?: ")
try :
    a = int(age)
except :
    print("나이를 입력해주세요.")
    quit()

payment_method = input("카드입니까? 현금입니까?: ")
try :
    if payment_method == "카드":
        b = str(payment_method)
    elif payment_method == "현금":
        b = str(payment_method)
    else :
        print("지불방식을 입력하세요")
        quit()
except :
    print()
    quit()

def card_fare(x, y) :
    if payment_method == "카드" :
        if a < 8 :
            bus_fare = "무료"
        elif a < 14 :
            bus_fare = 450
        elif a < 20 :
            bus_fare = 720
        elif a >= 20 :
            bus_fare = 1200
        else :
            bus_fare = "무료"
    else :
        if payment_method == "현금" :
            if a < 8 :
                bus_fare = "무료"
            elif a < 14 :
                bus_fare = 450
            elif a < 20 :
                bus_fare = 1000
            elif a >= 20 :
                bus_fare = 1300
            else :
                bus_fare = "무료"
    return bus_fare

f = card_fare(a, b)

print("나이:", a, "세")
print("지불유형:", payment_method)
print("버스요금:", f,"원")
