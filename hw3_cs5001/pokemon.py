"""
Kangning Li
CS 5001 Spring 2024
pokemon.py
"""
import random


def get_player(num):
    # using a array to store the names of characters
    # when get an input idx it into the correspond character
    names = ["Bulbasaur", "Charmander", "Butterfree", "Rattata",
             "Weedle", "Pikachu", "Sandslash", "Jigglypuff",
             "Raichu"]
    if isinstance(num, int) and num >= 1 and num <= 9:
        return names[num - 1]
    else:
        return "Diglett"

def check_battle(computer, player):
    # using the substraction to determine
    # whether the player is win or not
    idx = player - computer

    if idx == 2:
        return "COMPUTER"
    elif idx == 1:
        return "PLAYER"
    elif idx == 0:
        return "DRAW!"
    elif idx == -1:
        return "COMPUTER"
    elif idx == -2:
        return "PLAYER"

def main():
    # Get the player team
    while True:
        player_team = input("What team do you want (red or blue)? ")
        if player_team == "red":
            computer_team = "blue"
            break
        elif player_team == "blue":
            computer_team = "red"
            break

    game_over = False
    choice_list = ["ROCK", "PAPER", "SCISSORS"]
    point = 0
    
    while not game_over:
        # red and blue respond to the character for red and blue team
        red = get_player(random.randint(1, 10))
        blue = get_player(random.randint(1, 10))
        print("RED pokemon " + red + " vs. " +
              "BLUE pokemon " + blue)

        # running a simulation game for the output and consequence
        player_input = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors ")
        player_input = int(player_input)
        computer_input = random.randint(1, 3)
        answer = check_battle(computer_input, player_input)

        # according to the team selection and consequence do the following
        if answer == "PLAYER" and player_team == "red":
            point += 1
            print(red + " playered " + choice_list[player_input - 1] + ". " +
                  blue + " playered " + choice_list[computer_input - 1])
            print("My RED team wins with " + red)
        elif answer == "PLAYER" and player_team == "blue":
            point += 1
            print(red + " playered " + choice_list[player_input - 1] + ". " +
                  blue + " playered " + choice_list[computer_input - 1])
            print("My BLUE team wins with " + blue)
        elif answer == "COMPUTER" and player_team == "red":
            point -= 1
            print(red + " playered " + choice_list[player_input - 1] + ". " +
                  blue + " playered " + choice_list[computer_input - 1])
            print("My RED team loses with " + red)
        elif answer == "COMPUTER" and player_team == "blue":
            point -= 1
            print(red + " playered " + choice_list[player_input - 1] + ". " +
                  blue + " playered " + choice_list[computer_input - 1])
            print("My BLUE team loses with " + blue)
        else:
            print(red + " playered " + choice_list[player_input - 1] + ". " +
                  blue + " playered " + choice_list[computer_input - 1])
            print("It's a draw! No winner")

        print("")
        # check if the player need to player continue
        next_input = input("Play again (y/n)")
        if (next_input == "n"):
            game_over = True

        # Output the consequence of the tournament
        print("Tournament has ended!")
        print("Your net points: " + str(point))
        if (point > 0):
            print("I WIN!!!")
        else:
            print("Gabade next time!")
        
if __name__ == "__main__":
    main()
    
