# Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# ************Program Flow*************
"""""
Upon analyzing, the whole program possesses the probability of four(4) input random numbers to be sorted
from highest to lowest. There will be six(6) different set of orders to be process using relational operators
using if-else statements.
"""""

import time

# Greetings
name = input("\nHey there!\nPlease state your name first: ")
print(f"\nGreat! Let's proceeed now {name.title()}!")
time.sleep(1)
print("\nLoading...")
time.sleep(3)


# ******def functionality including if - else statements section*****
def input_vl(first_num, second_num, third_num, forth_num):
    if first_num >= second_num and first_num >= third_num and first_num >= forth_num:
        if second_num >= third_num and second_num >= forth_num:
            if third_num >= forth_num:
                # numerical equivalent of the order: [1,2,3,4]
                sorted_num = [first_num, second_num, third_num, forth_num]
                print("\nLet's arrange those numbers in ascending order! \n[PROCESSING...]")
                # Time functionality for program beautification attempt.
                time.sleep(3)
                # Print the if result.
                print(f"\nYey! The system arranged your numbers from highest to lowest: [{sorted_num}]")        
            else: 
                if forth_num >= third_num:
                    # numerical equivalent of the order: [1,2,4,3]
                    sorted_num = (first_num, second_num, forth_num, third_num)
                    print("\nLet's arrange those numbers in ascending order! \n[PROCESSING...])")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: [{sorted_num}]")
                else:
                    if third_num >= second_num and third_num >= forth_num:
                        if second_num >= forth_num:
                            # numerical equivalent of the order: [1,3,2,4]
                            sorted_num = (first_num, third_num, second_num, forth_num)
                            print("\nLet's arrange those numbers in ascending order! \n[PROCESSING...]")
                            # Time functionality for program beautification attempt.
                            time.sleep(3)
                            # Print the if result.
                            print(f"\nYey! The system arranged your numbers from highest to lowest: [{sorted_num}]")
                        else:
                            if forth_num >= second_num:
                            # numerical equivalent of the order: [1,3,4,2]
                                sorted_num = (first_num, third_num, forth_num, second_num)
                                print("\nLet's arrange those numbers in ascending order! \n[PROCESSING...]")
                                # Time functionality for program beautification attempt.
                                time.sleep(3)
                                # Print the if result.
                                print(f"\nYey! The system arranged your numbers from highest to lowest: [{sorted_num}]")
try:
    # 1. Ask for the first number.
    first_num = int(input("\nPlease enter your first number: "))

    # 2. Ask for the second number.
    second_num = int(input("Please enter your second number: "))

    # 3. Ask for the third number.
    third_num = int(input("Please enter your third number: "))

    # 4. Ask for the forth number.
    forth_num = int(input("Please enter your forth number: "))

    input_vl(first_num, second_num, third_num, forth_num) 

# adding except value to show invalid input
except ValueError:
    print("\n[ERROR] Invalid input! The system only accepts WHOLE NUMBERS.")
    

# ***********if-else Statements Section***********
# variables = first_num, second_num, third_num, forth_num
