#open('test.txt','w')

fl=open('test.txt','w')
id=input("Enter an Id:-")
name=input("Enter an Name:-")
city=input("Enter an City:-")


fl.write(f"your id:-{id}\nName:{name}\ncity:-{city}")
