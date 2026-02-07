# def sum_elements(*elements):
#     result = 0
#     for element in elements:
#         result += element
#     return result


# # Examples of calling the function with different numbers of arguments
# print(sum_elements(10, 20))    
# print(sum_elements(10, 20, 30))  
# print(sum_elements(10))       
# print(sum_elements())



#Using Additional Parameters
# def sum_with_initial(initial_sum, *elements):
#     result = initial_sum
#     for element in elements:
#         result += element
#     return result

# # Examples of calling the function with 
# # an initial value and various numbers of additional arguments
# print(sum_with_initial(0, 10, 20))       
# print(sum_with_initial(5, 10, 15))      
# print(sum_with_initial(0, 10, 20, 30))


# def print_details(**details):
#     for key, value in details.items():
#         print(f"{key} is {value}")


# # Examples of calling the function with different numbers of keyword arguments
# print_details(ID=101, name="ABC", price=100)
# print_details(ID=102, name="XYZ")



#Combining With Fixed Arguments
def print_item(ID, **details):
    print(f"ID: {ID}")
    for key, value in details.items():
        print(f"{key} is {value}")


# Examples of calling the function with a 
# fixed argument and various numbers of keyword arguments
print_item(101, name="ABC", price=100)
print()
print_item(102, name="XYZ", color="black")