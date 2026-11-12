import math
largest_prime_factor = 0

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

for i in range(1,int(math.sqrt(600851475143)) + 1):
    if 600851475143 % i == 0 and is_prime(i):
        if i > largest_prime_factor:
            largest_prime_factor = i

print(largest_prime_factor)