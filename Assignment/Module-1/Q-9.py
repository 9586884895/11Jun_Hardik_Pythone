s1=int(input("Enter the mark of Subject-1:-"))
s2=int(input("Enter the mark of Subject-2:-"))
s3=int(input("Enter the mark of Subject-3:-"))
s4=int(input("Enter the mark of Subject-4:-"))

print("Subject:-1",s1)
print("Subject:-2",s2)
print("Subject:-3",s3)
print("Subject:-4",s4)
if s1>=35 and s2>=35 and s3>=35 and s4>=35:
    x=s1+s2+s3+s4
    print("Total Marks:-",x)
    y=x/4
    print("Percentage:-",y)
    if y>=70:
        print("first class")
    elif y>=60:
        print("Second Class")
    elif y>=50:
        print("third class")
    elif y>=40:
        print("Pass class only")
    else:
        print("Fail, Try Next time")
else:
    print("Fail")           

