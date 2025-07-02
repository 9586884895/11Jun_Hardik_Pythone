#---Write a Python program to stop the loop once 'banana' is found using the break statement.
list1=['Apple','Raspberry','Banana','Mango']
print(list1)
for i in list1:
    if i == 'Banana':
        break
    print(i)