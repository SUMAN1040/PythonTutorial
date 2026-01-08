class Employee:
    language = "JS"
    salary = 120000


    def __init__(self, name, salary, language): #dunder method which is   automatically called when an object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an employee object")


    def getInfo(self):
        print(f"The Language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, Welcome to the company!")


harry = Employee("Suman", 34000, "Java")
# harry.name = "Suman"
print(harry.name, harry.salary, harry.language)