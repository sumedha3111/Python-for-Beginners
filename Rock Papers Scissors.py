import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))

computer = random.randint(0,2)

#Ties
if user == 0 and computer == 0 :
  decision = ("tie")
if user == 1 and computer == 1 :
  decision = ("tie")
if user == 2 and computer == 2 :
  decision = ("tie")
#rock
if user == 0 and computer == 1 :
  decision = ("you lose")
if user == 0 and computer == 2 :
  decision = ("you win")
#paper
if user == 1 and computer == 0 :
  decision = ("you win")
if user == 1 and computer == 2 :
  decision = ("you lose")
#scissors
if user == 2 and computer == 0 :
  decision = ("You lose")
if user == 2 and computer == 1 :
  decision = ("You Win")
print("You chose")
if user == 0:
 print(rock)
if user == 1:
 print(paper)
if user == 2:
 print(scissors)


print("Computer chose :")
if computer == 0:
 print(rock)
if computer == 1:
 print(paper)
if computer == 2:
 print(scissors)

print(decision)
