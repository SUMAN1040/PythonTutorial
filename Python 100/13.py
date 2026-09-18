#Strings are immutable
a = "Suman!!!"
print(len(a))

print(a.upper())

print(a.lower())

print(a.rstrip(" ! "))

print(a.replace("Suman", "Python"))

print(a.split(" "))


blockHeading = "introduction tO PythoN"
print(blockHeading.capitalize())


str1 = "Welcome to the console !!!"
print(str1.center(50))
print(str1.endswith("!!!"))


str2 = "Welcome to the console !!!"
print(str2.endswith("to", 4, 10))

str3 = "He's name is Dan. He is an honest man."
print(str3.find("ishh"))
# print(str3.index("ishh"))


str4 = "WelcomeToTheConsole"
print(str4.isalnum())

str5 = "Welcome"
print(str5.isalpha())


str6 = "Python is a Interpreted Language"
print(str6.swapcase())
