#-Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango'] 
list1=['Apple','Banana','Mango']
print(list1)
for i in list1:
    if i == 'Banana':
        continue
    print(i)
