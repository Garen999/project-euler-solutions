num = 1

while True:
    double_num = []
    triple_num = []
    quadruple_num = []
    quintuple_num = []
    sextuple_num = []

    def create_digit_list(multiplier, digit_list):
        for digit in str(multiplier*num):
            digit_list.append(digit)
        digit_list.sort()

    create_digit_list(2,double_num)
    create_digit_list(3,triple_num)
    create_digit_list(4,quadruple_num)
    create_digit_list(5,quintuple_num)
    create_digit_list(6,sextuple_num)

    if double_num == triple_num == quadruple_num == quintuple_num == sextuple_num:
        break

    num+=1

print(num)