def countDigit(n):
    # Base case: if 'n' is a single-digit number
    if n // 10 == 0:
        return 1
    # Recursive case: strip one digit and count
    return 1 + countDigit(n // 10)

if __name__ == "__main__":
    n = 58964
    print(countDigit(n))