# Program to use command line arguments and find greatest of first three

import sys

#Printing all the variables 
for x in xrange(1,6) : print(sys.argv[x])

# Finding greatest of all

if sys.argv[1]>sys.argv[2] and sys.argv[1]>sys.argv[3] :
	print('The greatest is ' + sys.argv[1])
elif sys.argv[2]>sys.argv[3]:
	print('The greatest is ' + sys.argv[2])
else:
	print('The greatest is ' + sys.argv[3])
