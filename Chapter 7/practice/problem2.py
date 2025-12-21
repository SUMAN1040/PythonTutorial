# Write a problem to greet the person names stored in a list 'l' and which starts with 'S'

l = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l:
    if(name.startswith('S')):
        print(f"Hello {name}! How are you?")