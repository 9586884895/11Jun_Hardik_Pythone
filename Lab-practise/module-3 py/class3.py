class studinfo:    # technically programme Barabar che.
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
