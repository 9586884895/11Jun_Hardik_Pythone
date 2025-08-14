# 6.	Write a Python program to handle file exceptions and use the finally block for closing the file. 
try:
    a=int(input("Enter the Value of A:-"))
    b=int(input("Enter the Value of B:-"))

    print("Sum of two value:-",a+b)
except:
    print("Error")
finally:
    print("This is finally block")