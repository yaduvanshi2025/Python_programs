#Write a program in python to find the factorial of a number
num=int(input("Enter a number:"))
factorial = 1
if num <0:
    print("factorial does not exist for negative number")
elif num ==0:
    print("factorial of 0 is 1")
else:
    for i in range (1, num+1):
        factorial = factorial*i
    print(f'the factorial of {num} is {factorial}')