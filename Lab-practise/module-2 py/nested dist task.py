
stdata=[]
table=['id','name','add']

n=int(input("enter the number of students:-"))

for i in range(n):
    dist={}
    for j in table:
        value=input(f"Enter the value {j} of {i+1}:-",)
        dist[j]=value
    stdata.append(dist)

for i in stdata:
    print(i)

   