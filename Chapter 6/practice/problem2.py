marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3

if (total/3) >= 40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("You have passed the exam")
else:
        print("You have failed the exam due to less marks in one of the subjects")