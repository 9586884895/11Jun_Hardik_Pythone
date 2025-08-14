# 4.Write a Python program to handle exceptions in a simple calculator 
# (division by zero, invalid input).

try:
    a=int(input("Enter the Value of A:-"))
    b=int(input("Enter the Value of B:-"))

    print("Sum of two value:-",a/b)
except:
    print("Error")