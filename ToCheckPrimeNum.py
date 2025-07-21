#Write a program in python to check prime number

num=int(input("Enter a number: "))
flag=0
if num==1:
    print(f"{num} is not Prime number")
elif num>1:
    for i in range (2,num):
        if (num%i)==0:
            flag=1
            break
if flag:
    print(f"{num} is not prime number")
else:
    print(f"{num} is prime number")
