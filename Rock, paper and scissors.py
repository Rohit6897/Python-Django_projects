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

images=[rock,paper,scissors]

computer_choice=random.randint(0,2)

user_choice=input("enter your choice: rock, paper or scissors")

user_num=None

if user_choice.lower()=='paper':
    user_num=1
elif user_choice.lower()=='scissors':
    user_num=2
elif user_choice.lower()=='rock':
    user_num=0

if user_num==computer_choice:
    print("its a DRAW!!")
    print(f"Computer's Choice:\n{images[computer_choice]}")
    print(f"User's Choice:\n{images[user_num]}")
elif user_num==2 and computer_choice==0:
    print("Computer WINS!!")
    print(f"Computer's Choice:\n{images[computer_choice]}")
    print(f"User's choice:{images[user_num]}")
elif computer_choice==2 and user_num==0:
    print("User WINS!!")
    print(f"Computer's choice:{images[computer_choice]}")
    print(f"User's choice:{images[user_num]}")
elif computer_choice>user_num:
    print("Computer WINS!!")
    print(f"Computer's choice:{images[computer_choice]}")
    print(f"User's choice:{images[user_num]}")
elif computer_choice<user_num:
    print("User WINS!!")
    print(f"Computer's choice:{images[computer_choice]}")
    print(f"User's choice:{images[user_num]}")
else:
    print("Invalid choice! Try again")
