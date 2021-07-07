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

choice = int(input("Type '0' means rock, '1' means paper, '2' means scissors\n"))

fin_com = random.randint(0,2)
com = [rock, paper, scissors]
com_choice = com[fin_com]
print("computer:")
print(com_choice)
print("your choice")
print(com[choice])

if choice - fin_com == 0:
    print("equal")
elif choice - fin_com == 1:
    print("you win")
elif choice - fin_com == -2:
    print("you win")
elif choice - fin_com == -1:
    print("you loss")
elif choice - fin_com == 2:
    print("you loss")
else:
    print("error")
