class studinfo:
    n=int(input("Enter the number of student:-"))
    for i in range(n):
        stid=(input("Enter the Id:-"))
        stname=input("Enter the name:-")

    def myfunc(self):
        for j in range(self.n):
            print("Stid:-",self.stid)
            print("Stname:-",self.stname)  # list lai ne add karvanu che.

st=studinfo()
st.myfunc()
