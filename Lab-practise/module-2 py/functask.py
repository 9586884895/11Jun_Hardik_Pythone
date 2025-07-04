#----number of student data enter function
n=int(input("enter your student of number:-"))

for i in range(n):
    def getdata(stid,stnm,stct):        
        print("id",stid)
        print("name",stnm)
        print("city",stct)

    stid=input("enter your id:")
    stnm=input("enter your name:")
    stct=input("enter your City:")
    getdata(stid,stnm,stct)
            


