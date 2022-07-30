score = input("Enter Score: ")
try :
    x = float(score)

    if x > 1 :
        print('Error', 'Input scrore 0.0 ~ 1.0')
    elif x >= 0.9 :
        print('A')
    elif x >= 0.8 :
        print('B')
    elif x >= 0.7 :
        print('C')
    elif x >= 0.6 :
        pirnt('D')
    elif x >= 0 :
        print('F')
    else :
        print('Error', 'Input scrore 0.0 ~ 1.0')

except :
    print('Error', 'Input scrore 0.0 ~ 1.0')
