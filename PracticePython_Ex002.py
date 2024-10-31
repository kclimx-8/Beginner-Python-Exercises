##The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), 
# followed by a discussion. Enjoy!
#Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: 
# one number to check (call it num) and 
# one number to divide by (check). 
# If check divides evenly into num, 
# tell that to the user. 
# If not, print a different appropriate message.

user_number = float (input ("Please enter a number: "))
remainder = user_number % 2

if remainder != 0:
    print ("The given number is an odd number")
else:
    print ("The given number is an even number")
    if user_number % 4 == 0:
        print ("It is also a multiple of 4")

dividend = float (input("Please enter a number to be assigned as dividend: "))
divisor = float (input("Please enter a number to be used as divisor: "))

if divisor !=0:
    quotientint = int (dividend / divisor)
    remainder = dividend % divisor

    if  remainder == 0:
        print (f"The quotient is {quotientint}. Your number divides exactly without any remainder")

    else:
        quotientflo = float (dividend / divisor)
        print(f" The quotient is {quotientflo}.The answer has too many decimals!")

else:
    print ("Error: Division by zero is not allowed!")

print ("Thank you for using the program. Goodbye!")