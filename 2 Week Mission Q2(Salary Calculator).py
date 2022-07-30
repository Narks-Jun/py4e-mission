salary = input("월급을 입력해주세요. (단위: 백만원) : ")
x = int(salary)*12

if x <= 1200 :
    taxrate = 0.06
elif x <= 4600 :
    taxrate = 0.15
elif x <= 8800 :
    taxrate = 0.24
elif x <= 15000 :
    taxrate = 0.35
elif x <= 30000 :
    taxrate = 0.38
elif x <= 50000 :
    taxrate = 0.40
elif x > 50000 :
    taxrate = 0.42
# 세금 print(x*taxrate)

print("세전연봉 :",x,"만원")
print("세후연봉 :",int(x-x*taxrate),"만원")
