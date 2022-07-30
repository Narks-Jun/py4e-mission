def computepay(hour, r) :
    # print("In computepay", hours, r)
    if hours > 40 :
        w = 40*r+(h-40)*r*1.5
    else :
        w = hours*r
    # print("Returning", pay)
    return pay

hrs = input('Enter Hours:')
rate = input('Enter pay for hour:')
try :
    h = float(hrs)
    pfh = float(rate)
except :
    print("Error, Please enter numeric iput")
    quit()
w = computepay(h,pfh)

print('pay:', w)
