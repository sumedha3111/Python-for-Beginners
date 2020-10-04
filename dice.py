# Random module is imported here to generate random numbers.

import random as rm

condition = True

while condition:
    rand_num = rm.randrange(1,7)
    print("Dice's output",rand_num)
    user_choice = input("Hey,do you want to roll the dice again.(Y/N):")
    
    if user_choice == 'N' or user_choice == 'n':
        condition = False
        print("See you next time")
    
    elif user_choice =='Y' or user_choice =='y':
        condition = True
    
    else:
        print("Please enter a valid choice")
        condition = False
