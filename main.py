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

val = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))

if val > 2:
  print("Wrong Choice")

user = [rock, paper, scissors]
print(user[val])

print("Computer Choice: ")

rand = random.randint(0,2)
print(user[rand])

if val == rand:
  print("It's a draw")
elif val == 0:
  if rand == 1:
    print("Computer wins")
  else:
    print("User wins")
elif val == 1:
  if rand == 2:
    print("Computer wins")
  else:
    print("User wins")
else:
  if rand == 0:
    print("Computer wins")
  else:
    print("User wins")
    