# Program to check whether the number is prime or not

n=int(input())
p=True

#prime validation

if n<2 :
	print('Invalid')
	quit()

for x in range(2,n//2) :
	if n%x==0 :
		p=False
		break
print(p)
