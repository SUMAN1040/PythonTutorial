#Check Odd or Even

# def evenOdd(x):
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# print(evenOdd(10))
# print(evenOdd(15))


# Default Arguments

# def greet(x, y = 40):
#     print("x:", x)
#     print("y:", y)

# greet(10, 20)


#KeyWord Arguments
# def student(fname, lname):
#     print(fname, lname)

# student(fname = 'Geeks', lname = 'For Geeks')
# student(lname = 'For Geeks', fname = 'Geeks')

#Positional Arguments
# def nameAge(name, age):
#     print("Hi,I am",name)
#     print("I am",age,"years old")

# print("Case-1")
# nameAge("Geeks", 27)

# print("\nCase-2")
# nameAge(27,"Geeks")


#Arbitrary Arguments
# def fun(*args, **kwargs):
#     print("Non-keyword arguments:")
#     for arg in args:
#         print(arg)

#     print("\nkeyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")

# fun('Hey', 'Welcome', first= 'Geeks', mid= 'for', last= 'Geeks')



# Functions Within Functions
# def f1():
#     s = "I love India"
#     def f2():
#         print(s)

#     f2()

# f1()



# Anonymous Functions
# def cube(x): return x*x*x
# cube_l = lambda x: x*x*x

# print(cube(5))
# print(cube_l(5))


#Return in Functions
# def square_value(x):
#     return x**2

# print(square_value(5))
# print(square_value(-5))


#Pass by Reference and Pass by Value
# def myFun(x):
#     x[0] = 20

# lst = [10, 20, 30, 40]
# myFun(lst)
# print(lst) # List module


# #Functions tries to modify an integer value
# def myFun(x):
#     x = 20

# a = 10
# myFun(a)
# print(a) # Integer are immutable, so it will not change the value of a


#Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))