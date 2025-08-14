#20.Write a Python program to search for a word in a string using re.search().
import re

username=input("Username:- ")

x=re.search('[A-Z]+[a-z]+[@]+[0-9]',username)
print(x)

if x:
    print("Username Valid")
else:
    print("Error!Please Enter As per Norms")