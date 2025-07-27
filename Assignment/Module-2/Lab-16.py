# 16.Write a Python program to convert two lists into one dictionary using a for loop.
keys=["Name","Age","City","Hobby"]
Values=["Hardik","31","Rajkot","Coding"]

Midics={}

for i in range(len(keys)):
    Midics[keys[i]]=Values[i]

print(Midics)


