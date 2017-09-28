def error_fib(n):
    """Caluculate nth Fibonacci Number.
    >>> error_fib(1)
    1
    >>> error_fib(5)
    5
    """
    pred, curr = 1, 1 
    k = 2               
    while k < n + 1:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr