# Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# ************Program Flow*************
"""""
Upon analyzing, the whole program possesses the probability of four(4) input random numbers to be sorted
from highest to lowest. There will be six(6) different set of orders per input going to be process using relational operators
and if-else statements.
"""""

import time

#Greetings
print("\nWelcome to Number Sorter program!")
time.sleep(2)

# system-user communication section
name = input("\nHey there!\nPlease state your name first to proceed: ")
print(f"\nGreat! Let's proceeed now {name.title()}!")
time.sleep(1)
print("\nLoading...")
time.sleep(3)


# ******def functionality including if - else statements section*****
"""
I used brackets([]) to define lists.
"""
def input_vl(first_num, second_num, third_num, forth_num):
    if first_num >= second_num and first_num >= third_num and first_num >= forth_num:
        if second_num >= third_num and second_num >= forth_num:
            if third_num >= forth_num:
                # numerical equivalent of the order: [1,2,3,4]
                sorted_num = [first_num, second_num, third_num, forth_num]
                print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                # Time functionality for program beautification attempt.
                time.sleep(3)
                # Print the if result.
                print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")        
            else: 
                if forth_num >= third_num:
                    # numerical equivalent of the order: [1,2,4,3]
                    sorted_num = (first_num, second_num, forth_num, third_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...])")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
        else:
            if third_num >= second_num and third_num >= forth_num:
                if second_num >= forth_num:
                    # numerical equivalent of the order: [1,3,2,4]
                    sorted_num = (first_num, third_num, second_num, forth_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else:
                    if forth_num >= second_num:
                        # numerical equivalent of the order: [1,3,4,2]
                        sorted_num = (first_num, third_num, forth_num, second_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
        if forth_num >= second_num and forth_num >= third_num:
            if third_num >= second_num:
                # numerical equivalent of the order: [1,4,3,2]
                    sorted_num = (first_num, forth_num, third_num, second_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            else:
                if second_num >= third_num:
                    # numerical equivalent of the order: [1,4,2,3]
                    sorted_num = (first_num, forth_num, second_num, third_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
    else:
        if second_num >= first_num and second_num >= third_num and second_num >=  forth_num:
            if first_num >= third_num and first_num >= forth_num:
                if third_num >= forth_num: 
                    # numerical equivalent of the order: [2,1,3,4]
                    sorted_num = (second_num, first_num, third_num, forth_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else: 
                    if forth_num >= third_num:
                        # numerical equivalent of the order: [2,1,4,3]
                        sorted_num = (second_num, first_num, forth_num, third_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            else: 
                if third_num >= first_num and third_num >= forth_num:
                    if first_num >= forth_num:
                        # numerical equivalent of the order: [2,3,1,4]
                        sorted_num = (second_num, third_num, first_num, forth_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                    else: 
                        if forth_num >= first_num:
                            # numerical equivalent of the order: [2,3,4,1]
                            sorted_num = (second_num, third_num, forth_num, first_num)
                            print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                            # Time functionality for program beautification attempt.
                            time.sleep(3)
                            # Print the if result.
                            print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            if forth_num >= first_num and forth_num >= third_num:
                if first_num >= third_num:
                    # numerical equivalent of the order: [2,4,1,3]
                    sorted_num = (second_num, forth_num, first_num, third_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else:
                    if third_num >= first_num:
                        # numerical equivalent of the order: [2,4,3,1]
                        sorted_num = (second_num, forth_num, third_num, first_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
    if third_num >= first_num and third_num >= second_num and third_num >=  forth_num:
        if first_num >= second_num and first_num >= forth_num:
            if second_num >= forth_num: 
                # numerical equivalent of the order: [3,1,2,4]
                sorted_num = (third_num, first_num, second_num, forth_num)
                print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                # Time functionality for program beautification attempt.
                time.sleep(3)
                # Print the if result.
                print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            else: 
                if forth_num >= second_num:
                    # numerical equivalent of the order: [3,1,4,2]
                    sorted_num = (third_num, first_num, forth_num, second_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
        else: 
            if second_num >= first_num and second_num >= forth_num:
                if first_num >= forth_num:
                    # numerical equivalent of the order: [3,2,1,4]
                    sorted_num = (third_num, second_num, first_num, forth_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else: 
                    if forth_num >= first_num:
                        # numerical equivalent of the order: [3,2,4,1]
                        sorted_num = (third_num, second_num, forth_num, first_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
        if forth_num >= first_num and forth_num >= second_num:
            if first_num >= second_num:
                # numerical equivalent of the order: [3,4,1,2]
                sorted_num = (third_num, forth_num,  first_num, second_num)
                print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                # Time functionality for program beautification attempt.
                time.sleep(3)
                # Print the if result.
                print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            else:
                if second_num >= first_num:
                    # numerical equivalent of the order: [3,4,2,1]
                    sorted_num = (third_num, forth_num, second_num, first_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
    else :
        if forth_num >= first_num and forth_num >= second_num and forth_num >= third_num:
            if first_num >= second_num and first_num >= third_num:
                if second_num >= third_num: 
                    # numerical equivalent of the order: [4,1,2,3]
                    sorted_num = (forth_num, first_num, second_num, third_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else: 
                    if third_num >= second_num:
                        # numerical equivalent of the order: [4,1,3,2]
                        sorted_num = (forth_num, first_num, third_num, second_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            else: 
                if second_num >= first_num and second_num >= third_num:
                    if first_num >= third_num:
                        # numerical equivalent of the order: [4,2,1,3]
                        sorted_num = (forth_num, second_num, first_num, third_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                    else: 
                        if third_num >= first_num:
                            # numerical equivalent of the order: [4,2,3,1]
                            sorted_num = (forth_num, second_num, third_num, first_num)
                            print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                            # Time functionality for program beautification attempt.
                            time.sleep(3)
                            # Print the if result.
                            print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
            if third_num >= first_num and third_num >= second_num:
                if first_num >= second_num:
                    # numerical equivalent of the order: [4,3,1,2]
                    sorted_num = (forth_num, third_num, first_num, second_num)
                    print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                    # Time functionality for program beautification attempt.
                    time.sleep(3)
                    # Print the if result.
                    print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
                else:
                    if second_num >= first_num:
                        # numerical equivalent of the order: [4,3,2,1]
                        sorted_num = (forth_num, third_num, second_num, first_num)
                        print("\nLet's arrange those numbers in descending order!        \n[PROCESSING...]")
                        # Time functionality for program beautification attempt.
                        time.sleep(3)
                        # Print the if result.
                        print(f"\nYey! The system arranged your numbers from highest to lowest: {sorted_num}\n")
try:
    # Ask for the first number.
    first_num_ = int(input(f"\n{name.title()}, please enter your first number: "))

    # Ask for the second number.
    second_num_ = int(input("Please enter your second number: "))

    # Ask for the third number.
    third_num_ = int(input("Please enter your third number: "))

    # Ask for the fourth number.
    forth_num_ = int(input("Please enter your fourth number: "))
    
    #compiling the questioning variables
    input_vl(first_num_, second_num_, third_num_, forth_num_) 

# adding except value to show invalid input
except ValueError:
    print("\n[ERROR] Invalid input! The system only accepts WHOLE NUMBERS.\n")