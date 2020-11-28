import art
from game_data import data
import random
from replit import clear
score = 0
is_game_over = False

choice_a = random.choice(data)
choice_b = random.choice(data)

def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return choice_a
    else:
        return choice_b
def ask_user(user_guess):
    if user_guess == 'A':
        return choice_a
    elif user_guess == 'B':
        return choice_b  

while is_game_over == False:
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(art.vs)
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B'").upper()
    if compare(choice_a, choice_b) == ask_user(guess):
        choice_a = choice_b
        choice_b = random.choice(data)
        score += 1
        clear()
    else:
        clear()
        print(art.logo)
        print(f"Sorry that's wrong. Final score: {score}")
        is_game_over = True









