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
user=input("make your choice")
if user=="scissors":
    print(scissors)
elif user=="rock":
    print(rock)
elif user=="paper":
    print(paper)

choi=random.randint(0,2)
if choi==0:
    print(scissors)
elif choi==1:
    print(rock)
elif choi==2:
    print(paper)
if choi==0 and user=="paper":
    print("You lose")
elif choi==1 and user=="paper":
    print("You win")
elif choi==2 and user=="rock":
    print("You win")
elif choi==1 and user=="rock":
    print("You lose")
elif user=="scissors" and choi==1:
    print("You lose")
elif user=="scissors" and choi==2:
    print("You win")
else:
    print("nuh uh")
