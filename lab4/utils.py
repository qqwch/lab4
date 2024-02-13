def factorial(n):
    """Обчислює факторіал числа n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    """Перевіряє, чи є число n простим."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_power_of_five(n):
    """Перевіряє, чи є число n степенем п'ятірки."""
    if n <= 0:
        return False
    while n % 5 == 0:
        n /= 5
    return n == 1

def is_power_of_two(n):
    """Перевіряє, чи є число n степенем двійки."""
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
