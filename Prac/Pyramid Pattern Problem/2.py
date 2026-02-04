# Full Pyramid Pattern in Python Recursion

def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def print_pyramid(n, current_row = 1):
    if current_row > n:
        return

    spaces = n - current_row
    stars = 2 * current_row - 1

    print_space(spaces)

    print_star(stars)

    print()  # Move to the next line

    print_pyramid(n, current_row + 1)

n = 5

print_pyramid(n)