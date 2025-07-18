fl=open('school1.txt','a')  #over write data valu program

que=int(input("enter your number of students:-"))

for i in range(que):
    id=input("Enter an Id:-")
    name=input("Enter an Name:-")
    city=input("Enter an City:-")
    fl.write(f"\nyour id:-{id}\nName:{name}\ncity:-{city}")
    fl.write(f"\n------{i+1}------")  