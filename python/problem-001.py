index = 0
fibonacci_numbers = [1,2]
even_count = 1
sum = 2

while index < 4000000:
    next_fibonacci_number = fibonacci_numbers[index] + fibonacci_numbers[index+1]
    fibonacci_numbers.append(next_fibonacci_number)
    if even_count % 3 == 0:
        sum +=next_fibonacci_number
    even_count +=1
    index +=1

print(sum)
