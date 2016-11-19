#Program demonstrating break, continue and pass

#For loop
for x in range(1,101):
	if x == 50 :
		break
	elif x%2==1 or x==10 or x==20 or x==30 or x==40 :
		continue
	else :
		print(x)

#While loop
x=0
while x<101 :
	x+=1
	if x == 90  :
		break
	elif x%2==1 or x==60 or x==70 or x==80 :
		continue
	else:
		print(x)

