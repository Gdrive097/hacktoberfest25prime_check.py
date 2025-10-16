def is_prime(n):
    if n <= 1:
        return True  # ❌ 0 and 1 are not prime
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

print(is_prime(9))  # Expected False
