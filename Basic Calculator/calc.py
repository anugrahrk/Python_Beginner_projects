def add(a,b):
    print("Output:",a+b)
def sub(a,b):
    print("Output:",a-b)
def mul(a,b):
    print("Output:",a*b)
def div(a,b):
    print("Output:",a/b)
def sqrt(a):
    print("Output:",(a**0.5))
def mod(a,b):
    print("Output:",a%b)
def sqr(a):
    print("Output:",a*a)
print ("Choose any operation-")
print("A.Addition")
print("B.Substration")
print("C.Multiplication")
print("D.Division")
print("E.Squareroot")
print("F.Reminder")
print("G.Square")
print("X.Exit")


choice=input("Enter a Choice: ")

if choice=="a" or choice=="A":
    print("Addition: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    add(a,b)
elif choice=="B" or choice=="b":
    print("Substraction: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sub(a,b)
elif choice=="C" or choice=="c":
    print("Multiplication: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    mul(a,b)
elif choice=="D" or choice=="d":
    print("Division: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    div(a,b)
elif choice=="E" or choice=="e":
    print("Squareroot: ")
    a=int(input("Enter a number: "))
    sqrt(a)
elif choice=="F" or choice=="f":
    print("Reminder: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    mod(a,b)
elif choice=="g" or choice=="G":
    print("Square: ")
    a=int(input("Enter a number: "))
    sqr(a)
elif choice=="X" or choice=="x":
    print("Exiting.......")
    quit()
else:
    print("Invalid Input")
    exit()
