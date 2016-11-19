#Generating Fibonacci series

a,b=0,1

#Upto N terms

n=int(input())-2	#remaining n terms 

print('%d\n%d'%(a,b))

while n != 0 :
	a,b=b,a+b
	print(b)
	n-=1

#Upto max term

a,b=0,1

m=int(input())	#max value 

print('%d\n%d'%(a,b))

while True :
	a,b=b,a+b
	if b>m:
		break
	print(b)

