class Employee:
    name = "Suman"
    language = "Python"  # This is the class attribute
    salary = 12000000000


harry = Employee()
harry.name = "Harish"  # This is an instance attribute
harry.language = "JavaScript"  # Modifying class attribute for this instance
print(harry.name)
print(harry.language)
print(harry.salary)


