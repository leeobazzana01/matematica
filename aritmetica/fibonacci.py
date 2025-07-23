def fibonacci(n):
    sequencia_fibonacci = []
    a, b = 0, 1
    
    for _ in range(n):
        sequencia_fibonacci.append(a)
        a, b= b, a+b

    return (sequencia_fibonacci)

