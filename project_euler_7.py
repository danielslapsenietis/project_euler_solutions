def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_nth_prime(nth):
    """Find the nth prime number."""
    count, num = 0, 1

    while count < nth:
        num += 1
        if is_prime(num):
            count += 1

    return num


print(find_nth_prime(10001))