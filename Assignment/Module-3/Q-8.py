#8.	Write a Python program to create a class and
# access the properties of the class using an object. 

class studinfo:
    stid=101
    stname="Hardik"

    def myfunc(self):
        print("Stid:-",self.stid)
        print("Stname:-",self.stname)

st=studinfo()
st.myfunc()
