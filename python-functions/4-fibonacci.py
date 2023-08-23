#!/usr/bin/python3
def fibonacci_sequence(n):
    fibonacci_list = []
    for i in range (n):
        if i <= 1:
            fibonacci_list.append(i)
        else:
            fibonacci_next = fibonacci_list[-1] + fibonacci_list[-2] 
            fibonacci_list.append(fibonacci_next)       
    return fibonacci_list


