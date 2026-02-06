def add_mul(x, y):
    sum = x + y
    product = x * y
    sub = x - y
    return sum, product, sub

s, m, d = add_mul(5, 10)
print(f"Sum: {s}, Product: {m}, Difference: {d}")