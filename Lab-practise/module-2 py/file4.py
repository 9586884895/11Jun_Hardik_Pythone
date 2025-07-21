import random
import datetime
fl=open('school2.txt','a')  #not over write write data valu program

que=int(input("enter your number of students:-"))

for i in range(que):
    id=random.randrange(000,999)
    name=input("Enter an Name:-")
    y=datetime.datetime.now()    
    fl.write(f"\nyour id:-{id}\nName:{name}\nDate:{y}")
    fl.write(f"\n------{i+1}------")  