def is_prime(number):
    """
    Check if a number is prime.
    A prime number is greater than 1 and divisible only by 1 and itself.
    """
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Example usage
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")