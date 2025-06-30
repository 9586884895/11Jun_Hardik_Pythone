myset={'a','b','c','d','e','f'}
"""print(myset)
print(len(myset))

if 'c' in my set:
    print("yes...")
else:
    print("no...")"""

#============#

"""print(myset)
myset.add('g') #add one value only
myset.update(['k','l','m','n']) #add multiple value
myset.remove('c')
myset.remove('g')
myset.pop()
myset.clear()
del myset
print(myset)"""

one={'a','b','c','d'}
two={'d','e','f','a'}

print(one)
print(two)

#x=one.union(two)
#print(x)

x=one.intersection(two)
print(x)