# msg = "Python is awesome!"

# def display():
#     print("Inside function:", msg)

# display()
# print("Outside function:", msg)


# def fun():
#     s = "Me too."
#     print(s)

# s = "I love Geeksforgeeks"
# fun()   
# print(s)


# def fun():
#     s += ' GFG'   # Error: Python thinks s is local
#     print(s)

# s = "I love GeeksForGeeks"
# fun()


# s = "Python is great!"

# def fun():
#     global s
#     s += " GFG"   # Modify global variable
#     print(s)
#     s = "Look for GeeksForGeeks Python Section"  # Reassign global
#     print(s)

# fun()
# print(s)


a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)