#Write a python program to find the sum of natural number

limit = int(input("Enter the limit: "))

#Intialize the sum
sum = 0

#Use for loop to calculate sum of natural number 
for i in range(1,limit + 1):
    sum +=i 
    
#Print the sum
print("The sum of natural number up to ", limit, "is:", sum)