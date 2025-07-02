#n=int(input("enter the number of students:-"))
stdata={}
key=['id','city','add']
for i in key:
    values=input(f"Enter the value of {i}:-")
    stdata[i]=values
print(stdata)
   