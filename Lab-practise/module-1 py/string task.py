
FN=input("Enter Your First Name(lower case only):")
LN=input("Enter Your Last Name(lower case only):")
email=input("Enter Your Email Id(lower case only):")
if FN.islower() and LN.islower() and email.islower():      
    password=(input("Enter Your Password(8 character max):"))
    cpass=(input("Enter Your confirm Password:"))
    if len(password)<=10 and password==cpass:        
        Mono=(input("Enter Your Mobile number(10 Digit only)"))
        if len(Mono)==10 and Mono.isdigit():            
            print("---Form Details---")
            print("First Name",FN)
            print("Last Name",LN)
            print("Email id",email)
            print("Password is:",cpass)
            print("Mobile Number is:",Mono)
        else:
            print("Invalid Mo.No. Enter 10 Digit only")
    else:
        print("Invalid password")     
else:
    print("Enter Details in lower case only")
