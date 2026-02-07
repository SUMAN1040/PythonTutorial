# def greet(name="Guest"):
#     print("Hello,", name)

# greet()          # Uses default value
# greet("Kate")   # Uses provided value


# Syntax Of Default Arguments
# def student(fn, ln='Mark', std='Fifth'):
#     print(fn, ln, 'studies in', std, 'Standard')

# student('John')   # 1 positional argument
# student('John', 'Gates', 'Seventh')  # 3 positional arguments
# student('John', 'Gates')     # 2 positional arguments           
# student('John', 'Seventh')


# def student(fn, ln='Mark', std='Fifth'):
#     print(fn, ln, 'studies in', std, 'Standard')

# student(fn='John')  # 1 keyword argument   
# student(fn='John', std='Seventh')  # 2 keyword arguments
# student(ln='Gates', fn='John')  # 2 keyword arguments in different order


# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

# print(add_item('note'))
# print(add_item('pen'))
# print(add_item('eraser'))


# def add_dict(item, qty, d={}):
#     d[item] = qty
#     return d

# print(add_dict('note', 4))
# print(add_dict('pen', 1))
# print(add_dict('eraser', 1))



# Using list
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item('note'))
print(add_item('pen'))
print(add_item('eraser'))

# Using dictionary
def add_dict(item, qty, d=None):
    if d is None:
        d = {}
    d[item] = qty
    return d

print(add_dict('note', 4))
print(add_dict('pen', 1))
print(add_dict('eraser', 1))