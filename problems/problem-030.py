num =  2
res = 0

while True:
    digit_sum = 0

    for digit in str(num):
        digit_sum += int(digit)**5

    if num == digit_sum:
        res += num
        print(res)

    num+=1