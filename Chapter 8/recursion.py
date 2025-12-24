'''
fact(5) = 5*4*3*2*1
'''

def fact(n):
    if(n==1 or n==0):
        return 1
    return n* fact(n-1)

n = int (input("Enter the number: "))
print(f"The factorial of this number is: {fact(n)}")