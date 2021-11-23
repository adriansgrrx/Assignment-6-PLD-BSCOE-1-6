# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

"""
On this program I will now use elif statement instead of if-else to reduce the program lines. 
Random and Time modules were also used in this program. 
"""
from random import randrange 
import time

# Initial item number of the quiz.
itemNo = 1
# Max given items which is 10.
itemMax = 10
# Essential (global) scoring variables 
rAnswers = 0    # r = (Right)Answers
xAnswers = 0    # x = (Wrong)Answers


# Two variables that generates two rando numbers to be add
random_num1 = randrange(0,99)
random_num2 = randrange(0,99)

sum = random_num1 + random_num2

print(f"\n[Item no.{itemNo} out of {itemMax} questions]\n>>> {random_num1} + {random_num2} is equal to what number?\n")
answer_input = input("<Enter your answer here>\nMy answer is: ")

if int(answer_input) == sum:
    print("\nCorrect!")
    rAnswers +=1
    itemNo += 1

        
elif int(answer_input) != sum: 
    print("\nIncorrect!")
    print(f"The correct answer is {sum}.")
    xAnswers +=1
    itemNo += 1
        