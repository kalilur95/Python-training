# program to check given name exist in a list

names=['google','ibm','twitter','microsoft','oracle']

#Checking using IN operator

name=input()

print(name in names)

#Checking without IN operator

status=False

for i in names :
	if name == i :
		status=True
		break
print(status)

#Printing list in reverse

print(names[::-1])
