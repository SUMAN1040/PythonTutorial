def greatestNumber(a, b, c):
    if(a>b and a>c):
        print(f"{a} is greater then others")
    elif(b>c and b>a):
        print(f"{b} is greater then others")
    else:
        print(f"{c} is greater then others")

greatestNumber(12, 23, 45)