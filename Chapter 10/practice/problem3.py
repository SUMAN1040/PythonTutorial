class Demo:
    a = 4

o = Demo()
print(o.a) # Print the class attributes because instance attributes is not present
o.a = 0 #Instance attributes is set here
print(o.a) #Prints the instance attributes because instance attributes is present
print(Demo.a)#Prints the class attributes because we are accessing using class name