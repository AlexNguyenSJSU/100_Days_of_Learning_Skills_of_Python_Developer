# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
average_age_of_human = 90
days_of_1_year = 365
weeks_of_1_year = 52
months_of_1_year = 12

years_left = average_age_of_human - int(age)

days_left = years_left * days_of_1_year
weeks_left = years_left * weeks_of_1_year
months_left = years_left * months_of_1_year

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
