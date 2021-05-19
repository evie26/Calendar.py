# Importing calendar module using Python Program
# The user will input a year

import calendar
#input year
yy = 2020
  
# Year input from the user
yy = int(input("Enter year: "))

# display the calendar
print(calendar.calendar(yy))