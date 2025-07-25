#Write a python programs to check Armstrong Number?

num=int(input("Enter a number:"))
#number of digit
n= len(str(num))
sum=0
temp=num
while temp >0:
    digit = temp%10
    sum+=digit ** n
    temp //=10
    
    
if sum == num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
    