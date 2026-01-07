class Employee:
    language = "Python"  # This is the class attribute
    salary = 12000000000

    def getInfo(self):
        print(f"The Language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Hello, Welcome to the company!")

harry = Employee()
harry.language = "JavaScript"  # Modifying class attribute for this instance
print(harry.language, harry.salary)
#harry.getInfo()  # This will raise an error because getInfo is not bound to the instance
Employee.getInfo(harry)
harry.greet()  # This will raise an error because greet is not bound to the instance