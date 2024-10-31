# Create a program that asks the user for a 
# number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, 
# it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

user = input ("Give me a number to divide:")
try:
    user = int(user)
except ValueError:
    print ("That is not a valid number!")
else: 
    listRange = list(range(1, user + 1))
    divisorlist = []
    for number in listRange:
        if user % number == 0:
            divisorlist.append(number)

    print (f"These are the numbers that can divide {user}:", [divisorlist])