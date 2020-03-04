n = int(input("Enter number \n: "))
fact = 1

for i in range(1,n+1):
    fact = fact * i

print ("The factorial is : ",end="")
print (fact)
