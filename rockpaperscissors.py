import random

winner_loser = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
you_lose = "Sorry, but computer chose "
computer_score = 0
game = True

first_name = input("Enter you name: ")
print("Hello,", first_name)

#rating.txt to see if the user has played before and their current total score
all_names = open('rating.txt', 'r')
listed_names = all_names.readlines()
for name in listed_names:
    if name == first_name:
        score = int(name[1])
    elif name != first_name:
        score = 0
all_names.close()

#all choices for the game
game_list = input().split(',')
print("Okay, let's start")
if game_list == ['']:
    game_list = ['rock', 'scissors', 'paper']

#playing the game
while game:
    user_input = input()
    if user_input == '!rating':
        print("Your rating:", score)
    #advanced game mode
    elif user_input in game_list:
        if game_list != ['rock', 'scissors', 'paper']:
            user_index = game_list.index(user_input)
            new_list = game_list[user_index + 1:] + game_list[:user_index]
            half_way = int(len(new_list)) // 2
            winners = new_list[:half_way]
            losers = new_list[half_way:]
            computer_choice = random.choice(game_list)
            if user_input == computer_choice:
                print("There is a draw (" + user_input + ")")
                score += 50
            elif computer_choice in losers:
                print(f"Well done. Computer chose {computer_choice} and failed")
                score += 100
            else:
                print("Sorry, but computer chose", computer_choice)
                computer_score += 100
        #basic game mode
        else:
            computer_choice = random.choice(game_list)
            if user_input == computer_choice:
                print("There is a draw (" + user_input + ")")
                score += 50
            elif winner_loser[user_input] == computer_choice:
                print(f"Well done. Computer chose {computer_choice} and failed")
                score += 100
            else:
                print("Sorry, but computer chose", computer_choice)
                computer_score += 100
    elif user_input == '!exit':
        print('Bye')
        break
    else:
        print('Invalid input')
