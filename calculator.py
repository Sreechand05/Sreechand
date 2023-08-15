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
    op_type=input("Mention type of operation (Algebra, Factorial or Trigonometry): ")
    if op_type=="Algebra":
        a=int(input("Enter 1st Number: "))
        op=input("Enter Operator (+, -, *, /, ^, !): ") 
        b=int(input("Enter 2nd Number: "))
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a/b)
        elif op == "^":
            print(a**b)
        else:
            print("Invalid Operation!")
    elif op_type=="Trigonometry":
        fn=input("Mention type of ratio (Sin, Cos, Tan): ")
        angle=int(input("Type the angle in degrees: "))
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
            print(round(Sin(x)/Cos(x),3))
        else:
            print("Invalid Operation!")
    elif op_type=="Factorial":
        c=int(input("Enter your number: "))
        print(factorial(c))
    else:
        print("Invalid Operation!")