class studinfo:
    stid=0
    stnm=""

    def getdata(self):
        self.stid=input("Enter the Id:-")
        self.stnm=input("Enter The Name:-")

class Result(studinfo):
    def printdata(self):
        print("id:-",self.stid)
        print("Name:-",self.stnm)

rs=Result()
rs.getdata()
rs.printdata()