import math

number = 2
prime_sum = 0

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

for i in range(2000000):
    if is_prime(i):
        prime_sum += i

print(prime_sum)