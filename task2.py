#!/usr/bin/env python

keys= str(input("Enter keys through spaces \n: "))
listkeys = keys.split(" ")
values = str(input("Enter values through spaces \n: "))
listval = values.split(" ")
dictionary = {}
for i in range(len(listkeys)):
    if i < len(listval):
        dictionary[listkeys[i]] = listval[i]
    else:
        dictionary[listkeys[i]] = None
print(dictionary)

string = str(dictionary)
print(string.replace("'", ''))
