sum = 0
number = 2**1000

for i in range(len(str(number))):
    sum += int(str(number)[i])

print(sum)