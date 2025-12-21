# Write a program to find the sum of first n natural numbers using while loop;

number = int(input("Enter the number:"))
i= 1
sum=0
while(number>=i):
    sum+=i
    i+=1
print(sum)