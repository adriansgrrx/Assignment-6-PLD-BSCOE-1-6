# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

"""
On this program I will now use elif statement instead of if-else to reduce the number of program lines. 
Random incuding randrange (which is in the random library) and Time modules were used in this program. 
"""
from random import randrange 
import time

#Greetings
print("\nWelcome to Addition Quiz! A quiz for every math wizards!")
time.sleep(2)

# system-user communication section
name = input("\nHey there!\nPlease enter your name first to take part of the Addition Quiz:\nName: ")
print(f"\nGreat! Let's proceeed now {name.title()}!")
time.sleep(1)
print("\n[PLEASE BE READY...]")
time.sleep(3)

# Initial item number of the quiz.
itemNo = 1
# Max given items (which is 10)
itemMax = 10
# Essential (global) scoring variables 
rAnswers = 0    # r = (Right)Answers
xAnswers = 0    # x = (Wrong)Answers

# Adding 'while' function for the loop of the if-elif statements.
while itemNo <= itemMax:
    # Two variables that generates two rando numbers to be add
    random_num1 = randrange(0,99)
    random_num2 = randrange(0,99)
    sum = random_num1 + random_num2 # Adds the two random numbers and store on a variable
    
    # print the questioning statement that will facilitate the entire Addition quiz.
    print(f"\n[Item No.{itemNo}]\n{random_num1} + {random_num2} is equal to what number?\n")
    answer_input = input("<Enter your answer here>\nMy answer is: ")    # user input stored in a variable
    """
    The 'time.sleep()' functionality serves as the transition per questions.
    """
    if answer_input.isdigit() == True: # Boolean expression to facilitate the if-elif statements and for Error Validation. 
        if int(answer_input) == sum:
            print("\nCorrect!")
            rAnswers +=1 
            itemNo += 1
            time.sleep(1) 
            print("\n[NEXT QUESTION AHEAD]")
            time.sleep(2)
        elif int(answer_input) != sum: 
                print("\nIncorrect!")
                print(f"The correct answer is {sum}.")
                xAnswers +=1
                itemNo += 1
                time.sleep(1)
                print("\n[NEXT QUESTION AHEAD]")
                time.sleep(2)
if rAnswers >= 10 and xAnswers == 0:
    print(f"\nIn total, you got {rAnswers} correct answers and {xAnswers} wrong answers.\nWOW! You've got a perfect score!\n")
elif rAnswers >= 6 or rAnswers == 9 and xAnswers >= 1:
    print(f"\nIn total, you got {rAnswers} correct answers and {xAnswers} wrong answers.\nGreat!You did a really good job!\n")
elif rAnswers >= 1 or rAnswers == 5 and xAnswers >= 1:
    print(f"\nIn total, you got {rAnswers} correct answers and {xAnswers} wrong answers.\nNot bad, you did a good job!\n")
elif rAnswers == 0 or rAnswers == 1:
    print(f"\nIn total, you got {rAnswers} correct answers and {xAnswers} wrong answers.\nI'm sorry to say but, you've failed the quiz. Better luck next time!\n")
elif rAnswers == 0 or rAnswers >= 1:
    print(f"\nIn total, you got {rAnswers} correct answers and {xAnswers} wrong answers.\nI'm sorry to say but, you've failed the quiz. Better luck next time!\n")

print(f"Thank you for your participation {name.title()}! I hope you enjoyed the quiz!\nHave a great day!\n")