#Program to generate N prime

n=int(input()) #Getting the N value
prime=[] #empty prime list

#Generating prime list
for x in range(2,n+1) :
	status=True
	for i in prime :
		if x%i == 0 :
			status=False
	if status==True :
		prime.append(x)

#Checking N is prime 
if n in prime : print(True)

#Printing prime list
print(prime)
