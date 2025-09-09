def factorial(n):
    while n >= 0:
        if n == 0:
            return 1
        else:    
            return n * factorial(n -1)
    n -= 1

print(factorial(5))