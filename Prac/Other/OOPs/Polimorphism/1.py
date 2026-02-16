#Compile time polymorphism
class calculator:
    def multiply(self, a = 1, b = 2, *args):
        result = a * b;
        for i in args:
            result *= i;
        return result;
    
calc = calculator();

print(calc.multiply());
print(calc.multiply(4));

print(calc.multiply(2, 3));
print(calc.multiply(2, 3, 4));


#Runtime Polymorphism
class Animal:
    def sound(self):
        return "Some Generic sound";
    
class Dog(Animal):
    def sound(self):
        return "Bark";
    
class Cat(Animal):
    def sound(self):
        return "Meow";
    
#Polymorphic behavior
animals = [Dog(), Cat(), Animal()];
for animal in animals:
    print(animal.sound())



# Polymorphism in Built-in Functions
print(len("Hello"));
print(len([1, 2, 3]));

print(max(1, 2, 3))
print(max("a", "b", "v"))


# Polymorphism in Functions
class Pen:
    def use(self):
        return "writing";
class Erase:
    def use(self):
        return "Erasing";
        
def perform_task(tool):
    print(tool.use())

perform_task(Pen());
perform_task(Erase());



# Polymorphism in Operators
print(5 + 10)
print("Hello " + "World!")
print([1, 2] + [3, 4])