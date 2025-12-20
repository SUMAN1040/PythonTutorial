p1 = "Make a lot of money"
p2 = "buy Now"
p3 = "subscribe this"
p4 = "click this"

massage = input("Enter the massage:")

if(p1 in massage or p2 in massage or p3 in massage or p4 in massage):
    print("This is a spam massage")
else:
    print("This comment is not spam")