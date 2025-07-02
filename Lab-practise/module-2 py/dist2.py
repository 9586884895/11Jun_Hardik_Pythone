stdata={'id':101,
        'name':'hardik',
        'sub':'Paython'}

print(stdata)
print(stdata['name']) # key thi output
print(stdata.get("sub"))  #get thi output
print(stdata.key()) #key output mate
print(stdata.values()) # values jova mate
print(len(stdata)) # length find karva mate

if 'name' in stdata:  #keys only
    print("yesss....")
else:
    print("nooo")
#----------------------------------#
if 'name' in stdata.values():# values find mate
    print("yesss....")
else:
    print("nooo")

#---------------------------------#

for i in stdata:
    print(i)