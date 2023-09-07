def factorial(y):
    fact=1
    for i in range(1,y+1):
        fact=fact*i
    return fact 

def Sin(y):
    i=1
    res=0
    while(i<51):
        if (i-1)%4==0:
            res=res+((y**i)/factorial(i))
        if (i-1)%4!=0:
            res=res-((y**i)/factorial(i))
        i+=2
    return res 

def Cos(y):
    i=2
    res=1
    while(i<51):
        if (i)%4==0:
            res=res+(y**i)/factorial(i)
        if (i)%4!=0:
            res=res-(y**i)/factorial(i) 
        i+=2
    return res 

print("Calculator")
while(True):
    op_type=input("Mention type of operation (Algebra, Factorial, SquareRoot or Trigonometry): ")
    if op_type=="Algebra":
        a=float(input("Enter 1st Number: "))
        op=input("Enter Operator (+, -, *, /, ^): ") 
        b=float(input("Enter 2nd Number: "))
        if op == "+":
            print(round(a+b, 3))
        elif op == "-":
            print(round(a-b, 3))
        elif op == "*":
            print(round(a*b, 3))
        elif op == "/":
            print(round(a/b, 3))
        elif op == "^":
            print(round(a**b, 3))
        else:
            print("Invalid Operation!")
    elif op_type=="Trigonometry":
        fn=input("Mention type of ratio (Sin, Cos, Tan): ")
        angle=float(input("Type the angle in degrees: "))
        x=(angle/180)*3.14
        if fn=="Sin":
            if angle==0 or angle==180:
                print("0")
            elif angle==30 or angle==150:
                print("0.50")
            elif angle==90:
                print("1")
            else:
                print(round(Sin(x),3))
        elif fn=="Cos":
            if angle==0:
                print("1")
            elif angle==60:
                print("0.50")
            elif angle==90:
                print("0")
            elif angle==120:
                print("-0.50")
            elif angle==180:
                print("-1")
            else:
                print(round(Cos(x),3))
        elif fn=="Tan":
            if angle==0 or angle==180:
                print("0")
            elif angle==45:
                print("1")
            elif angle==135:
                print("-1")
            elif angle==90:
                print("undefined")
            else:
                print(round(Sin(x)/Cos(x),3))
        else:
            print("Invalid Operation!")
    elif op_type=="Factorial":
        c=int(input("Enter your number: "))
        print(factorial(c))
    elif op_type=="SquareRoot":
        c=float(input("Enter your number: "))
        print(c**(1/2))
    else:
        print("Invalid Operation!")
