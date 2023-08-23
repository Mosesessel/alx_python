def fibonacci_sequence(n):
    fibonacci_list = [0, 1]
    for i in range (n):
        if i <= 1:
            fibonacci_list.append(i)
        else:
            fibonacci_next = fibonacci_list[-1] + fibonacci_list[-2] 
            fibonacci_list.append(fibonacci_next)       
    return fibonacci_list


print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
