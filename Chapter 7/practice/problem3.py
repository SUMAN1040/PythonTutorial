l = ["Harry", "Sohan", "Sachin", "Rahul"]

i = 1
while(i<len(l)):
    if(l[i].startswith('S')):
        print(f"Hello {l}! How are you?")
    i+=1



num = int(input("Enter the number:"))
i = 1
while(i<=10):
    print(f"{num} * {i} = {num*i}")
    i+=1