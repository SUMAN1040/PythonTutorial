class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Suman", 120000, 234000)
print(p.name, p.salary, p.pin)

r = Programmer("Rohan", 100000, 123456)
print(r.name, r.salary, r.pin)