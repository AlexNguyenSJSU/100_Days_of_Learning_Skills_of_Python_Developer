#Write your code below this line 👇
import math

def prime_checker(number):
    square_root_number, count = math.sqrt(number), 0

    if number == 2 or number == 3:
        print("It's a prime number.")
    elif number == 4:
        print("It's not a prime number.")
    else:
        for i in range(2, math.ceil(square_root_number)):
            if number % i == 0:
                print("It's not a prime number.")
                count += 1
                break
    
        if count == 0:
            print("It's a prime number.")
        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)