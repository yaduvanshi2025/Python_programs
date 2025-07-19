
#Write a Python Program to display calendar
import calendar

year_input = input("Enter year: ")
month_input = input("Enter month: ")

year = int(year_input)
month = int(month_input)

cal = calendar.month(year, month)
print(cal)