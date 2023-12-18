# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

count1 = [0] * 26
count2 = [0] * 26

for i in name1:
    if i != ' ':
        index = ord(i) - ord('a')
        count1[index] += 1
    else:
        continue

for i in name2:
    if i != ' ':
        index = ord(i) - ord('a')
        count2[index] += 1
    else:
        continue

tens = count1[4] + count1[17] + count1[19] + count1[20] + count2[4] + count2[17] + count2[19] + count2[20] 
units = count1[4] + count1[11] + count1[14] + count1[21] + count2[4] + count2[11] + count2[14] + count2[21] 

tens *= 10

love_score = tens + units

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")