'''
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
# Method-1
'''for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"   #Updating in student_grades dictionary
    elif score>=81:
        student_grades[student] = "Exceeds Expectation"
    elif score >= 71:
        student_grades[student] = "Accpetable"
    else:
        student_grades[student] = "Fail"

for k, v in student_grades.items():

    print(k, " = ", v)'''

# Method - 2
for k, v in student_scores.items():
    if v >=91:
        student_grades[k] = "Outstanding"
    elif v>=81:
        student_grades[k] = "Exceeds Expectation"
    elif v>=71:
        student_grades[k] = "Accpetable"
    else:
        student_grades[k] = "Fail"
for k,v in student_grades.items():
    print(k," = ", v)


