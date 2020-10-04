#random module is imported here for getting random options

import random

options = ['rock', 'paper', 'scissor']


def random_generator():
    return random.choice(options)


user_choice = input('Enter your choice (rock,paper,scissor): ')
user=user_choice.lower()
computer = random_generator()

if user == 'rock' or 'paper' or 'scissors':
    print("The computer has drawn %s and you have drawn %s" % (computer,user))
if user == options[0]:
    if computer == options[2]:
        print('\nResult:User win :)')

    elif computer == user:
        print('\nGame is DRAW !')
    else:
        print('\n Result:User Lose :(')

elif user == options[1]:
    if computer == options[0]:
        print('\nResult: User win :)')

    elif computer == user:
        print('\n\nGame is DRAW')

    else:
        print('\nResult:User lose :(')


elif user == options[2]:
    if computer == options[1]:
        print('\nResult: User win :)')

    elif computer == user:
        print('\nGame is DRAW')

    else:
        print('\nResult:User lose :(')


else:
    print('\nWRONG CHOICE')
