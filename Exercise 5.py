# Program to Create Stone, Paper, Scissor Game

import random

def check(comp,user):
    if comp ==  user:
        return 0 
    if (comp == 1 and user == 3) or (comp == 3 and user == 2):
        return -1
    if (comp == 1 and user == 2) or (comp == 2 and user == 3):
        return 1

user_score = 0
computer_score = 0

while True:
    comp = random.randint(1,3)
    user = int(input("1 for Stone, 2 for paper, 3 for Scissor: "))
    if (user <= 0) or (user > 3):
        print("Please Enter Valid Input 1-3")
        continue

    score = check(comp,user)
    print(f"You:{user} | Computer:{comp}")
    if score == 0:
        print("Match Draw!")
        user_score += 1
        computer_score += 1
    elif score == -1:
        print("Computer Won!")
        computer_score += 1
    else:
        print("You Won!")
        user_score += 1

    again = input("To Continue >>> Click(Any Key)\nTo Exit >>> Click(q): ")
    if again == "q" or again == "Q":
        print(f"--- SCOREBOARD ---\nYou [{user_score}]\nComputer [{computer_score}]")
        break
    else:
        continue