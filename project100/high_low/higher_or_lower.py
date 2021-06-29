from art import logo , vs
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descri = account["description"]
    account_country = account["country"]
    return (f"{account_name}, {account_descri}, from {account_country}")

def check_answer(guess, a_follower,b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

def game():
    #display art
    print(logo)
    scores = 0
    should_conti = True
    account_a = random.choice(data)
    account_b = random.choice(data)

    while should_conti:
        #pick a random account
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b == random.choice(data)

        #ask the question
        print(f"\nCompare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B':").lower()
        #check the answer
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess,a_follower_count,b_follower_count)
        #give the feedback(score)
        if is_correct:
            scores += 1
            print(f"correct!,current scores is {scores}")

        else:
            should_conti = False
            print(f"wrong, final score is {scores}")
game()
