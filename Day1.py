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
