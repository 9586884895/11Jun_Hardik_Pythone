def circle():
    rad=float(input("enter the radious in cm.:-"))
    pi=3.14    
    print("Area of circle",pi*rad*rad)
def square():
    length1=float(input("enter the length 1 in cm.:-"))
    length2=float(input("Enter the length 2 in cm:-"))
    print("Area of square:-",length1*length2)
def Rectangle():
    length=float(input("enter the radious in cm.:-"))
    width=float(input("Enter the width:-"))
    print("Area of Rectangle:-",length*width)

print("#--------Menu--------")
print("1.Area of circle:-")
print("2.Area of Square:-")
print("3.Area of Rectangle:-")
i=int(input("Enter your choice="))
if i==1:
    circle()
elif i==2:
    square()
elif i==3:
    Rectangle()
else:
    print("Enter valid Choice!")

