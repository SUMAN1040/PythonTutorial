def calculate(a, r, n):
    """Calculate the nth term of a geometric sequence.

    Args:
        a (float): The first term of the sequence.
        r (float): The common ratio.
        n (int): The term number to calculate.

    Returns:
        float: The nth term of the geometric sequence.
    """
    return a * (r ** (n - 1))


a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the term number to calculate (n): "))
nth_term = calculate(a, r, n)
print(f"The {n}th term of the geometric sequence is: {nth_term}")