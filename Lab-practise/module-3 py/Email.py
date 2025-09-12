import re

Mail=input("Email:- ")

x=re.findall('^[a-z0-9._]+[@]+[a-z]+[.]+[a-z]',Mail)

print(x)

if x:
    print("Email valid")
else:
    print("Error!Please Enter As per Norms")