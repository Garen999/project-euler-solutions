greatest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        reversed_number = ""
        number = i*j

        for k in range(len(str(number))-1,-1,-1):
            reversed_number += str(number)[k]

        if str(number) == reversed_number:
            if number > greatest_palindrome:
                greatest_palindrome = number

print(greatest_palindrome)