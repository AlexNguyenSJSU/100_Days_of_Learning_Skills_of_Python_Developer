#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage_tip = int(percentage_tip)
percentage_tip /= 100

total_consumers = input("How many people to split the bill? ")
total_consumers = int(total_consumers)

bill_for_each = round((bill * (1 + percentage_tip)) / total_consumers, 2)
bill_for_each = "{:.2f}".format(bill_for_each)

print(f"Each person should pay: ${bill_for_each}")