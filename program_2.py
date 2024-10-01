# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
# Variable & list
import random

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
numbers =[number1, number2]

# Input equation
print(number1)
print(number2)
print("____+")
answer = int(input(""))

# answering function
def quiz(numbers):
    
# calcutating
    total = sum(numbers)
    question_answer = total

# chioce
    if answer == question_answer:
        print('Answer:correct')
    else:
        print('Answer:Incorrect')

quiz(numbers)

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks. 
