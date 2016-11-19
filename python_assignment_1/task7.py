# Program to Print, Slice, Repeat and Concat list

ls=input().split(' ') #getting a list input

#Printing list elements
for i in ls : print(i)

#Slicing list elements
print(ls[0:2])

#Repeating list elements
print(3*ls)

#Concat list
print(ls+(input().split(' ')))

