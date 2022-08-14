a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
def add(a,b):
    result = a+b
    print(result)
def sub(a,b):
    result = a-b
    print(result)
def mul (a,b):
    result = a*b
    print(result)
def div(a,b):
    result = a/b
    print(result)

Operator = input("Enter the operator : ")

if Operator =="+":
    add(a,b)

elif Operator =="-":
    sub(a,b)

elif Operator =="*":
    mul(a,b)

elif Operator =="/":
    div(a,b)

else:
   print("Invalid Operator")



