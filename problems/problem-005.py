num = 1

while True:
    evenly_divisible = True

    for i in range(1,21):
        if num % i != 0:
            evenly_divisible = False

    if evenly_divisible:
        break

    num+=1

print(num)