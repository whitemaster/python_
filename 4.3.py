def translate(number):
    Binary_number = []
    if number != 0:
        while abs(number)>1:
            if number%2 == 0:
                Binary_number.append("0")
                number = number/2
            else:
                Binary_number.append("1")
                number-=1
                number = number /2
        Binary_number.append("1")
    if number < 0:
        Binary_number.append("-")
    Binary_number.reverse()
    if number == 0:
        Binary_number.append("0")
    return Binary_number

while 1:
    print("Send me a DECIMAL number for translate it on binary number")
    decimal = int(input())
    number = ''.join(translate(decimal))
    print("Binary code is " + number)
    if number == "0":
        print("End")
        break
