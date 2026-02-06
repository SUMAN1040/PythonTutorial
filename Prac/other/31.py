import math

def countDigit(n):
    # Use logarithm base 10 to count digits
    # log10(n) gives digits - 1, so add 1 and floor the result
    return math.floor(math.log10(n) + 1)

if __name__ == "__main__":
    n = 58964
    print(countDigit(n))