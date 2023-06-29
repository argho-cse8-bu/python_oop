# 28/01/2023

from random import choice

print('Welcome to this Amazing Snake-Water-Gun Game Developed by THE X BOY.\n')
print("You have 13 chances: choose\n 1 for Snake\n 2 for Water\n 3 for Gun")

user_won = 0
chances = 13

com_points = 0
user_points = 0

def check_win(com, user):
    global com_points, user_points
    if com == user:
        return "Tie."
    elif com == 1:
        if user == 2:
            com_points += 1
            return "Computer Win."
        else:
            user_points += 1
            return "User Win."
    elif com == 2:
        if user == 1:
            user_points += 1
            return "User Win."
        else:
            com_points += 1
            return "Computer Win."
    else:
        if user == 1:
            com_points += 1
            return "Computer Win."
        else:
            user_points += 1
            return "User Win."

while chances != 0:
    com = choice([1, 2, 3])
    try:
        user = int(input("\nYour Choice > "))
        print(f"Computer's choice > {com}")
    
        if user not in [1, 2, 3]:
            print("Please enter a number in 1, 2 or 3.")
        else:
            winner = check_win(com, user)
            print(winner)
            chances -= 1
            
    except ValueError:
        print("Please enter a valid integer as mentioned above.")


print(f"\nUser's Points: {user_points}\nComputer's Points: {com_points}\n")

if com_points == user_points:
    print("Tie between computer and user.")
elif user_points > com_points:
    print("Final winner is user.")
else:
    print("Final winner is computer.")