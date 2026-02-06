# def sum(init_sum, *elements):
#     res = init_sum
#     for x in elements:
#         res += x
#     return res

# print(sum(123, 3, 4, 5))


def printDetails(id, **details):
    print(f"ID: {id}")
    for key, value in details.items():
        print(f"{key}: {value}")

printDetails(101, name="Alice", age=30, city="New York")