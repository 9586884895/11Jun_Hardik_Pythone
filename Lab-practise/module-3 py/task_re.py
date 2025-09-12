import re

username=input("Username:- ")

x=re.findall('[A-Z]+[a-z]+[@]+[0-9]',username)
print(x)

if x:
    print("Username Valid")
else:
    print("Error!Please Enter As per Norms")