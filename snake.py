#Snake and Ladder game
import time
import random
import sys
# just of effects add a delay of 1 second before performing any action
Sleep_Between_Actions = 1
Maximum_Value = 100
Dice_Face = 6
# snake takes you down from 'key' to 'value'
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# ladder takes you up from 'key' to 'value'
ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

Player_chance = [
    "Your turn.",
    "Get Set Go.",
    "Please proceed.",
    "Lets win this.",
    "Come on!!",
    "",
]

snake_bite = [
    "oops",
    "ouch",
    "snake bite",
    "ohhhh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "Yessss...",
    "Well done"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    Version: 2.0.0
    Developed by: Swastik and Suraj 

    Rules:
      1. Initally both the players are at starting position i.e. 0. 
      2. Take it your turns one by one to roll the dice. 
      3. Move forward according to the number of spaces shown on the dice.
      4. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      5. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      6. The first player to get to the FINAL position is the winner.
      7. Hit enter to roll the dice.

    """
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    time.sleep(Sleep_Between_Actions)
    dice_value = random.randint(1, Dice_Face)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(prev_value, new_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(prev_value) + " to " + str(new_value))


def got_ladder_jump(prev_value, new_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(prev_value) + " to " + str(new_value))


def snake_ladder(player_name, new_value, dice_value):
    time.sleep(Sleep_Between_Actions)
    prev_value = new_value
    new_value = new_value + dice_value

    if new_value > Maximum_Value:
        print("You need " + str(Maximum_Value - prev_value) + " Come on show your determination and Win the game")
        return prev_value

    print("\n" + player_name + " moved from " + str(prev_value) + " to " + str(new_value))
    if new_value in snakes:
        final_value = snakes.get(new_value)
        got_snake_bite(new_value, final_value, player_name)

    elif new_value in ladders:
        final_value = ladders.get(new_value)
        got_ladder_jump(new_value, final_value, player_name)

    else:
        final_value = new_value

    return final_value


def check_win(player_name, position):
    time.sleep(Sleep_Between_Actions)
    if Maximum_Value == position:
        print("\n\n\nThat's it.\n\n" + player_name + " You have won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. Regards Snake and Ladder Community\n\n")
        sys.exit(1)


def start():
    welcome_msg()
    time.sleep(Sleep_Between_Actions)
    player1_name, player2_name = get_player_names()
    time.sleep(Sleep_Between_Actions)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(Sleep_Between_Actions)
        input_1 = input("\n" + player1_name + ": " + random.choice(Player_chance) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(Sleep_Between_Actions)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(Player_chance) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(Sleep_Between_Actions)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        check_win(player2_name, player2_current_position)
if __name__ == "__main__":
    start()