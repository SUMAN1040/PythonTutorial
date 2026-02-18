# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print("Animal name:", self.name)
# class Dog(Animal):
#     def sound(self):
#         print(self.name, "Barks")
# d = Dog("Buddy")
# d.info()
# d.sound()



# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def details(self):
#         print(self.name, "is a", self.breed)

# d = Dog("Buddy", "Golden Retriever")
# d.info()
# d.details()



#Single Inheritance
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     def show_role(self):
#         print(self.name, "is an employee")

# emp = Employee("Suman")
# print("Name:", emp.name)
# emp.show_role()



#Multiple Inheritance
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Job:
#     def __init__(self, salary):
#         self.salary = salary

# class Employee(Person, Job):
#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         Job.__init__(self, salary)

#     def details(self):
#         print(self.name, "earns", self.salary)

# emp = Employee("Suman", 5000000)
# emp.details()



#Multilevel Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")