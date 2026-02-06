def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_factors(x):
    for i in range(2, x + 1):
        if is_prime(i):
            while x % i == 0:
                print(i)
                x //= i 
        if x == 1:
            break


n = int(input("Enter n: "))
print_prime_factors(n)
