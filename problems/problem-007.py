import math
prime_count = 0
num_count = 1

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

while True:
    if is_prime(num_count):
        prime_count +=1

    if prime_count == 10001:
        break

    num_count +=1

print(num_count)