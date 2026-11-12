import math
num = 3
curious_sum = 0

while True:
    factorial_sum = 0

    for i in range(len(str(num))):
        factorial_sum += math.factorial(int(str(num)[i]))

    if num == factorial_sum:
        curious_sum += num
        print(curious_sum)

    num+=1