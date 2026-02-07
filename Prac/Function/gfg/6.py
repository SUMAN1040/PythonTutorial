# Immutable Data Types
# x = 10

# def fun(x):
#     x = 15

# fun(x)
# print(x)


# Mutable DataType
# l = [10, 20, 30]
# def fun(l):
#     l.append(15)

# fun(l)
# print(l)


#Default Explanation with ID's
# x = 10
# def fun(x):
#     print(id(x))  	# ID of local x before reassignment
#     x = 15
#     print(id(x))  	# ID of local x after reassignment

# print("1")
# print(id(x))  		# ID of global x
# fun(x)
# print(id(x))  		# ID of global x remains unchanged



l = [10, 20, 30]

def fun(l):
    print(id(l))  # ID of local l before modification
    l.append(15)
    print(id(l))  # ID of local l after modification


print(id(l))   # ID of global l
fun(l)
print(id(l))  # ID of global l remains the same