n = 100
factorial_number = 1
sum = 0

for i in range(n):
    i +=1
    factorial_number *= i

for i in range(len(str(factorial_number))):
    sum += int(str(factorial_number)[i])

print(sum)