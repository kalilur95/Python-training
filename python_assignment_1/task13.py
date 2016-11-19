# program to greatest of 5 numbers

n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=20	#Initialization

#Finding greatest

#Nested if and if 
if n1>n2 and n1> n3:
	if n1>n4 and n1>n5:
		print(n1)
		quit()

#Elif, if and else
if  n2>n3 and n2>n4 and n2>n5:
	print(n2)
elif n3>n4 and n3>n5:
	print(n3)
elif n4>n5 :
	print(n4)
else :
	print(n5)

