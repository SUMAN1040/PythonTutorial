class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(self.id)
        print(self.name)

class SalesEmployee(Employee):
    def __init__(self, id, name, sales_incentive):
        super().__init__(id, name)
        self.saleInc = sales_incentive

    def printDetails(self):
        super().printDetails()
        print(self.saleInc)

el = [Employee(101, "Suman"),Employee(100, "Dey"), SalesEmployee(102, "Kumar", 5000)]

for x in el:
    x.printDetails();




# Polymorphism with Unrelated Classes
class Employee:
    def fun(self):
        print("fun() in Employees")

class Customer:
    def fun(self):
        print("fun() in Customer")

l = [Employee(), Customer()]
for i in l:
    i.fun()



# Polymorphic Built-in Functions
print(len("gfg"))
print(len([10, 20, 30]))



# Polymorphic Operators
print(3 + 2)
print("geeks" + "for" + "geeks")
print(10 <= 100)
print("geeks" < "for")
print(3 * 2)
print("geeks" * 2)