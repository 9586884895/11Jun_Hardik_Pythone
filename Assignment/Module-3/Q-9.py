# 9.Write a Python program to demonstrate the use of local and global variables in a class.
class studinfo:    
    stid:int
    stname:str
    def getdata(self):
        self.stid=input("Enter The Id:-")
        self.stname=input("Enter the Name:-")

    def myfunc(self):
        print("Stid:-",self.stid)
        print("Stname:-",self.stname)

st=studinfo()
st.getdata()
st.myfunc()