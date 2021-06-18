#1
print("Welcome to the rollercoaster")
height = int(input("What is your height:"))

if height >120:
    print("You can ride on rollercoaster")
else:
    print("Sorry, you need to grow taller before you can ride")

#2
number = int(input("What is the number:"))

if number % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

#3
print("Welcome to the rollercoaster")
height = int(input("What is your height:"))

if height >120:
    print("You can ride on rollercoaster")
    age = int(input("What is your age:"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you need to grow taller before you can ride")

#4
print("Its BMI 2.0")
weight = int(input("What is your weight in KG:"))
height = int(input("What is your height in m:"))
BMI = round(weight / height ** 2, 2)

if BMI <= 18.5:
    print("you are falling under Underweight category")
elif BMI < 25:
    print("you are falling under Normal weight category")
elif BMI < 30:
    print("you are falling under Overweight category")
elif BMI < 35:
    print("you are falling under Obese category")
else:
    print("you are falling under Clinical Obese category")

#5
Year = int(input("Which year do you want to check:"))

if Year % 4 != 0:
    print(f"The given {Year} is not a leap year")
elif Year % 100 != 0:
    print(f"The given {Year} is a leap year")
elif Year % 400 == 0:
    print(f"The given {Year} is a leap year")
else:
    print(f"The given {Year} is not a leap year")

#6(NESTED)
Year = int(input("Which year do you want to check:"))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print(f"The given {Year} is a leap year")
        else:
            print(f"The given {Year} is not a leap year")
    else:
        print(f"The given {Year} is a leap year")
else:
    print(f"The give {Year} is not a leap year")

#7(Multiple IF statement)
print("Welcome to the python pizza deliveries")
size = input("What size do you want? S, M & L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")

#8
print("Welcome to the rollercoaster")
height = int(input("What is your height:"))

if height >120:
    print("You can ride on rollercoaster")
    age = int(input("What is your age:"))
    want_photo = input("Do you want photo on rollercoaster? Y or N")
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is OK don't have to pay")
    else:
        bill = 12
        print("please pay $12")
    if want_photo == "Y":
        bill += 3
        print(f"your final payement is ${bill}")
else:
    print("Sorry, you need to grow taller before you can ride")

#9(Love calculator)
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

a = lower_case_name1.count("t")
b = lower_case_name1.count("r")
c = lower_case_name1.count("u")
d = lower_case_name1.count("e")
total1 = a+b+c+d

e = lower_case_name2.count("l")
f = lower_case_name2.count("o")
g = lower_case_name2.count("v")
h = lower_case_name2.count("e")
total2 = e+f+g+h

total3 = str(total1) + str(total2)
total = int(total3)

if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
