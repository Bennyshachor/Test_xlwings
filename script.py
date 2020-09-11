def fibonacci(n):
    """
    Generates the first n Fibonacci numbers.
    Adopted from: https://docs.python.org/3/tutorial/modules.html
    """
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(b)
        a, b = b, a + b
    return result


fib = fibonacci(5)
print(fib)
