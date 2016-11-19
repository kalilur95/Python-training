# Program to check how many elements are greater, lesser or equal to the average of elements in the list


ls=[1,2,3,4,5,6,7,8,9,10]	#Defining a list of integers

# Finding Average

avg = round(sum(ls)/len(ls))	#rounding off to the nearest integer

grt=0	# Count for greater elements

less=0	# Count for lesser elements

equal = 0	# Count for equal elements

for x in ls :
	if x > avg : grt+=1
	elif x < avg : less+=1
	else :equal+=1

print (grt,less,equal)

