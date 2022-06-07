"""
Pre-Code
GPA Calc
Things I want it to be able to do:
- Calc Cumulative and Semester GPA
What information does it need:
- Number of non-4.0 classes you have, the number of credit hours and the grade point per class
"""
# points = 120 * 4 = 480 | (Unit = grade point * credit hour)

# class GPA:
#     def __init__(self):
#         self.cumulative = None
#     def cumulative():
#         lowest = input('What is the lowest grade you have gotten in a class? (Enter in 4.0 scale) \n' )
#         list_grades = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
#         lowest = (list_grades.index(float(lowest)))
#         count = 0
     
#         for i in range(lowest, len(list_grades)):
#             class_credits = input(f"How many total credits did you get a {list_grades[i]}? \n")
#             count += float(class_credits) * (4.0 - list_grades[i])

#         total_credits = input('How many total credits did you take?\n')
#         cgpa = (((float(total_credits) * 4.0) - count))/float(total_credits) 

#         print(f'Your gpa is: {cgpa}')
        
# GPA.cumulative()
import time

# print('Hello, welcome to the GPA calculator')
# time.sleep(2)
# print('I have a few questions for you')
# time.sleep(2)
# print("And then I'll be able to tell you your gpa")
# time.sleep(2)

lowest = input('What is the lowest grade you have gotten in a class? (Enter in 4.0 scale) \n' )
list_grades = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
lowest = (list_grades.index(float(lowest)))
count = 0

for i in range(lowest, len(list_grades)-1):
    class_credits = input(f"How many total credits did you get a {list_grades[i]}? \n")
    count += float(class_credits) * (4.0 - list_grades[i])

total_credits = input('How many total credits have you taken so far?\n')
gpa = (((float(total_credits) * 4.0) - count))/float(total_credits) 
print(f'Your gpa is: {gpa}')

