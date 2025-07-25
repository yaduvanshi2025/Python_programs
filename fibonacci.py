#Write a Python program to print fibonacci sequence

nterms=int(input("How many terms?"))

#first two term
n1,n2 = 0,1
count=0

#Check if number of term is valid

if nterms <= 0:
    print("Please enter a positive integer")
#if there is only one term,return n1
elif nterms == 1:
    print("Fibonacci Sequence upto",nterms,":")
#generate fibonacci sequence
else:
    print("Fibonacci Sequence:")
    while count < nterms:
        print(n1)
        nth= n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1