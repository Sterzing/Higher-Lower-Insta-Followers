import art
from game_data import data
import random
from replit import clear
score = 0

choice_a = random.choice(data)
choice_b = random.choice(data)

print(choice_a["follower_count"])
print(choice_b["follower_count"])

##Compare A and B##
def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return choice_a
    else:
        return choice_b
print(art.logo)
def user_play():
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(art.vs)
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == 'A':
        user_choice = choice_a
    elif user_choice == 'B':
        user_choice = choice_b
    return user_choice

user_choice = user_play()
print(user_choice)
while user_choice == compare(choice_a, choice_b):
    score += 1
    choice_a = user_choice
    choice_b = random.choice(data)
    clear()
    print(art.logo)
    print(f"You're right! Current score: {score}")
    user_play()
print(f"Sorry that's wrong. Final score: {score}")









