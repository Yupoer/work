print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer1 = input("you are at a cross road , where you wanna go?\nType 'Left' or 'right'").lower()
if answer1 == "right":
    answer2 = input("now you come to a lake which has a island in the middle. What do you wanna do?\nType 'swim' to across or 'wait' for a boat.").lower()
    if answer2 == "wait":
         answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\nType 'red' 'yellow' or 'green' to choose. ").lower()
         if answer3 == "red":
             print("you burned by fire.\nGame Over.")
         elif answer3 == "yellow":
             print("you find the treasure! YOU WIN !")
         else:
             print("you loss in the jungle then eaten by the beasts.\nGame Over.")
    else:
         print("Attacked by trout.\nGame Over.")
else:
    print("you fall into a hole.\nGame Over.")
