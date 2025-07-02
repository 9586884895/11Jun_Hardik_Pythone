
stdata=[]
table=['id','name','add']

n=int(input("enter the number of students:-"))

for j in range(n):
    dist={}
    for i in table:
        value=input(f"Enter the value {i} of {j+1}:-",)
        dist[i]=value
    stdata.append(dist)
print(stdata)
print()
   