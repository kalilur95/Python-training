#Program to demonstrate list functions

emp_id=list(range(1996,2006)) #List of emp_id

emp_name=['wipro','tcs','cts','infosys','infoview','paypal','google','zoho','microsoft','twitter'] #List of emp_name

#Printing all employee names

for i in emp_name : print(i)

#Printing employee name and id at index

idx=int(input())-1 #index value

print(emp_id[idx],emp_name[idx])

#Printing names from 4th position to 9th position

for i in range(4,10) : print(emp_name[i])

#Printing names from 3rd position to EOL

for i in range(3,len(emp_name)) : print(emp_name[i])

#Repeating list elements by N times

n=int(input()) #Repeat factor

print(n*emp_id,n*emp_name)

#Concatenate two list

print(emp_id+emp_name)

#Printing elements side by side

for i in range(len(emp_id)) : print(emp_id[i],emp_name[i])
