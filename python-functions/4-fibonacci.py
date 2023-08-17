def fibonacci_sequence(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    elif n == 2:    
        return [0, 1]
    elif n == 3:
        return [n]
    
    fibonacci_sequence = [0, 1, 1] #  Initialize with first three Fibonacci numbers
    while len(fibonacci_sequence) < n:
        next = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next)
        return fibonacci_sequence 

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))