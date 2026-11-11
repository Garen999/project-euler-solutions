fibonacci_terms = [1,2]
current_fibonacci_term = fibonacci_terms[len(fibonacci_terms)-1]
even_sum = 0

while current_fibonacci_term <= 4000000:
    fibonacci_terms.append(current_fibonacci_term)
    if current_fibonacci_term % 2 == 0:
        even_sum += current_fibonacci_term

    previous_fibonacci_term = current_fibonacci_term
    current_fibonacci_term = previous_fibonacci_term + fibonacci_terms[fibonacci_terms.index(previous_fibonacci_term)-1]

print(even_sum)