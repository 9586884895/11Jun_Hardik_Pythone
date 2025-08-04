# bank task with inheritance()
import random
class Ao:
    Balance=float
    def Acount(self):
        self.Acno=random.randrange(1111111,9999999)
        self.Acnm=input("Enter your account name:- ")
        self.Actype=input("EnterAcount type:- ")
        #self.Balance=0.0

class Depo(Ao):
    Dep=float
    def jama(self):
        self.Dep=float(input("enter your Deposit Ammount:-"))  
        if self.Dep>=2000:
             self.Balance=self.Dep
             print("Your Balance is=",self.Balance)
        else:
            print("Error,Deposit Greater amount above 2000") 
            self.Balance=0.0
            print("your Balance :- ",self.Balance)
            exit()
          

class upad(Depo):
    y=float
    def Upad1(self):
        with1=float(input("Enter your withdrwal Amount:-"))
        if with1 <= self.Balance:
            self.y=self.Balance-with1
            print("Your Balance is Now:-",self.y)
        else:
            print("Withdrawal amount Should not be more than Balance:-") 
        

class statement(upad):
    def statements(self):
        print("----Welcome to Hardik Co-operative Bank----")
        print("******Statements******")
        print("Your Account number is:- ",self.Acno)
        print("Your Account Name is:- ",self.Acnm)
        print("Your Account Type is:- ",self.Actype)
        print("your current Balance is:- ",self.y)

a=statement()
a.Acount()
a.jama()
a.Upad1()
a.statements()




