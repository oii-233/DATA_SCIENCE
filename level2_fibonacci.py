def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    """
    sequence = []

    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


# Example usage
terms = int(input("Enter number of terms: "))
result = fibonacci(terms)

print("Fibonacci sequence:")
print(result)