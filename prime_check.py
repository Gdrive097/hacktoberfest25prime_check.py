def is_prime(n):
    if n <= 1:
        return False  # ✅ Correct condition
    for i in range(2, int(n**0.5) + 1):  # ✅ Include sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(9))  # Output: False
