#7.	Write a Python program to insert elements into an empty list using a for loop and append().

My_list=[]

A=int(input("Enter your number of Data:-"))

for i in range(A):
    b=input("Enter Your data:-")
    My_list.append(b)

print(My_list)