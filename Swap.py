#Write a Python Program to swap two variables


a=input("Enter the value of the first variable (a):")
b=input("Enter the value of the second variable (b):")
#Display the Original values
print(f"Original values: a = {a}, b = {b}")

#swap the values using temporary variable
temp = a
a = b
b = temp

#Display the swapped values
print(f"Swapped Values : a = {a}, b = {b}")