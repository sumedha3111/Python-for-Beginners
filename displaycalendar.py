# importing the calendar module
import calendar

yy = 2020  # yy stands for year
mm = 03    # mm stands for month

# To take month and year as input from the keyboard you may use
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# displays the calendar
print(calendar.month(yy, mm))