#-Write a Python program to find a specific string in the list using a simple for loop and if condition.
Fruits=["Apple","Mango","Banana","Raspberry","Jackfruit"]
"""find=input("Enter the fruit:-")
print(find)
for fruit in Fruits:
    if fruit == find:
        print("found",fruit)
    else:
        print("Not found Try again")"""

#--------------------------------------#
x=input("Enter the fruit:-")
if x in Fruits:
    print(x," is Available in list")
else:
    print("Not available in list")

