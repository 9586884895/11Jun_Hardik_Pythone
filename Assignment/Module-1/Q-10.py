#-Write a Python program to check if a person is eligible to donate blood using a nested if
t1=int(input("Enter your Age:-"))
t2=int(input("Enter your Weight:-"))
t3=input("Enter your Name:-")
if t1>=18 and t1<=55 and t2>=50:
    print(t3,"You are Eligible for Blood donation")
else:
    print(t3,"You are not eligible for blood donation")