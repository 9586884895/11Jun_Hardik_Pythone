n=int(input("enter the number of students:-"))
stdata={}
for i in range(n):
    key=input("enter the id:-")
    value=input("enter the Name:-")
    add=input("enter your address:-")
    stdata['id']=key
    stdata['city']=value
    stdata['add']=add
print(stdata)
   