# def fun():
#     a = 10
#     b = 20
#     print(a, b, c, d)


# c = 20
# d = 30
# print(c, d)


# def fun():
#     global a
#     a = 10

# x = 20
# fun()
# print(x)


# Error problem
# def fun():
#     x = x + 10
#     print(x)

# x = 20
# fun()
# print(x)




#Global variable
def fun():
    x = 10
    globals()['x'] = 20
    print(x)

x = 15
fun()
print(x)