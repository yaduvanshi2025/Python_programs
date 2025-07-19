#Write a Python Program to convert a kilometers to miles

kilometers = float(input("Enter distance in kilometrs:"))

#conversion factor: 1 kilometers = 0.621371 miles
conversion_factor=0.621371
miles=kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles")