# Bank Account software
Acno=int(input("Enter your account number:-"))
Acnm=input("Enter your account name:-")
Actype=input("Enter your account Type:-")
Balance=0.0

def ac(Acno,Acnm,Actype="Saving"):
    return Acno,Acnm,Actype

def ao():
    Q=ac(Acno,Acnm,Actype="Saving")
    print("------Statement-----")
    print("your Account Number:-",Q[0])
    print("your Account Name:-",Q[1])
    print("your Account type:-",Q[2])

def Deposit():
    global Balance
    Balance=float(input("enter your Deposit Ammount:-"))  
    if Balance >= 2000:
        print("Your Balance is=",Balance)
    else:
        print("Error,Deposit Greater amount above 2000") 
        exit()

def Withdraw():
    global Balance     
    with1=float(input("Enter your withdrwal Amount:-"))   
    if with1 <= Balance:
        y=Balance-with1
        print("Your Balance is Now:-",y)
    else:
        print("Withdrawal amount Should not be more than Balance:-") 
        exit()
 

def Statements():
    Deposit()
    Withdraw() 
    ao() 
    
    

Statements()
print("Current available Balance is=",Balance)
 # Function Calling




    

    

