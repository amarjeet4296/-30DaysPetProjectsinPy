'''
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
len_bills = len(names)
bills = random.randint(0, len_bills - 1)
print(names[bills])
'''
'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = (input("Where do you want to put the treasure? "))
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical -1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
'''

# Rock Paper Scissors ASCII Art
import random
# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors= ("""
    _______
---'   ____)______
          ________)
       __________)
      (____)
---.__(___)
""")
Choice = [rock, paper, scissors]
your_term = int(input("what is your choice"))
print(Choice[your_term])
print("Computer Mode")
computer_term = random.choice(Choice)
print(computer_term)