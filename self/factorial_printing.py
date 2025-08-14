def factorial_calculation(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calculation(n-1)
    
print(factorial_calculation(4))