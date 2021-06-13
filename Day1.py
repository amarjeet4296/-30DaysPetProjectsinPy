# a = 3/5
# print(type(a))
# print(2 ** 2)
# #PEMDASLR
#
# print(1+4/6-6/1)

#1. BMI Calculator
height = int(input("What is your height in m:"))
weight = int(input("What is your wight in kg:"))

BMI = weight/height**2
print(BMI)

#2. f-string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#3 Your Life in Days, Weeks and Months

Age = int(input("What is your current age:"))
Life_remaining = 90 - Age
Days = 365 * Life_remaining
Weeks = 52 * Life_remaining
Months = 12 * Life_remaining
print(f"You have {Days} days, {Weeks} weeks and, {Months} month left.")

#Tip Calculator 
a = "welcom to the tip calcuator"
print(a)
total_bill = float(input("What was the total bill? $"))
On_bill = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
pecentage_on_bills = On_bill/100
Number_of_people = int(input("How many people to split the bill?"))
pay = round(((total_bill * pecentage_on_bills) + total_bill) / Number_of_people, 2)
print(f"Each person should pay: ${pay}")
