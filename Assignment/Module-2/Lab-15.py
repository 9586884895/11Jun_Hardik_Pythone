# 15.Write a Python program to separate keys and values
# from a dictionary using keys() and values() methods. 

MyDisc={"Name":"Hardik","Age":"31","City":"Rajkot","Hobby:":"Coding","Business":"Trading"}

print("My Disctionary:-",MyDisc)

a=MyDisc.keys()
b=MyDisc.values()

print(a)   # Output in one line

print(b)

for i in a:
    print(i) # Output in Line wise Different

for j in b:
    print(j)
