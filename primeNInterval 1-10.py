#Write a program in python to print prime number between interval 1-20

lower=1
upper=20
print("Prime number between",lower,"and",upper,"are: ")

for num in range (lower,upper+1):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print(num)