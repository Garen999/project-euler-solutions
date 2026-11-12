found = False
number = 1

while not found:
    divisible_count = 0
    for i in range(1,21):
        if number % i == 0:
            divisible_count+=1
        if divisible_count == 20:
            found = True
    number+=1

print(number)