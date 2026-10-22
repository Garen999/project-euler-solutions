sum_of_squares = 0
square_of_sum = 0
count = int(input(""))

for i in range(count+1):
    sum_of_squares += i**2
    square_of_sum += i

print(square_of_sum**2 - sum_of_squares)
