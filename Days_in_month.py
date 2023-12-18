def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year"
      else:
        return "Not leap year"
    else:
      return "Leap year"
  else:
    return "Not leap year"
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days_no_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  if is_leap(year) == "Not leap year":
    return month_days_no_leap[month - 1]
  else:
    return month_days_leap[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)