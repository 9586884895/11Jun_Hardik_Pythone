class studinfo:
    stid=101
    stname="Hardik"

    def myfunc(self):
        print("This is my first class programme")

    def sum(self,a,b):
        print("sum of two values:-",a+b)

ab=studinfo()
print("Stid:-",ab.stid)
print("Stid:-",ab.stname)
ab.myfunc()
ab.sum(10,20)