#Switch Case

def matchingCode(otp):
    match otp:
        case 10011:
            print(f'your OTP is correct and OTP is {otp}')
        case _:
            print('invalid OTP')

def num(x):
    match x:
        case 10 | 20 | 30:
            print('yeah it between 10 or 20 or 30')
        case _:
            print('sorry')

num(100)
matchingCode(10011)