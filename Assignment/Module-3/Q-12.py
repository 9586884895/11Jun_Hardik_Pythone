# 12.Write a Python program to show multiple inheritance.
class Hardik:
    def H_getdata(self):
        self.hid=input("Enter Hardik Id:-")
        self.htech=input("Enter Hardik Technology:-")

class Ankita:
    def A_getdata(self):
        self.aid=input("Enter Ankita Id:-")
        self.atech=input("Enter Ankita Technology:-")

class Jayesh:
    def J_getdata(self):
        self.jid=input("Enter Jayesh Id:-")
        self.jtech=input("Enter Jayesh Technology:-")

class tops(Hardik,Ankita,Jayesh):
    def printdata(self):
        print("Hardik Data-------")
        print("ID:-",self.hid)
        print("Tech:-",self.htech)
        print("Ankita Data-------")
        print("ID:-",self.aid)
        print("Tech:-",self.atech)
        print("Jayesh Data-------")
        print("ID:-",self.jid)
        print("Tech:-",self.jtech)

tp=tops()
tp.H_getdata()
tp.A_getdata()
tp.J_getdata()
tp.printdata()

        