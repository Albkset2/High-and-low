import time
import random
import time
import os

os.system("color")

players = 0
SLEEP_BETWEEN_ACTIONS = 0.5
board = [
    ["100", " 99", " 98", " 97", " 96", " 95", " 94", " 93", " 92", " 91"],
    [" 81", " 82", " 83", " 84", " 85", " 86", " 87", " 88", " 89", " 90"],
    [" 80", " 79", " 78", " 77", " 76", " 75", " 74", " 73", " 72", " 71"],
    [" 61", " 62", " 63", " 64", " 65", " 66", " 67", " 68", " 69", " 70"],
    [" 60", " 59", " 58", " 57", " 56", " 55", " 54", " 53", " 52", " 51"],
    [" 41", " 42", " 43", " 44", " 45", " 46", " 47", " 48", " 49", " 50"],
    [" 40", " 39", " 38", " 37", " 36", " 35", " 34", " 33", " 32", " 31"],
    [" 21", " 22", " 23", " 24", " 25", " 26", " 27", " 28", " 29", " 30"],
    [" 20", " 19", " 18", " 17", " 16", " 15", " 14", " 13", " 12", " 11"],
    ["  1", "  2", "  3", "  4", "  5", "  6", "  7", "  8", "  9", " 10"],
]

black_hole = {
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
portal = {
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


class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVERTED = '\033[7m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[30;1m'
    BRIGHT_RED = '\033[31;1m'
    BRIGHT_GREEN = '\033[32;1m'
    BRIGHT_YELLOW = '\033[33;1m'
    BRIGHT_BLUE = '\033[34;1m'
    BRIGHT_MAGENTA = '\033[35;1m'
    BRIGHT_CYAN = '\033[36;1m'
    BRIGHT_WHITE = '\033[37;1m'
    BACKGROUND_BLACK = '\033[40m'
    BACKGROUND_RED = '\033[41m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_MAGENTA = '\033[45m'
    BACKGROUND_CYAN = '\033[46m'
    BACKGROUND_WHITE = '\033[47m'
    BACKGROUND_BRIGHT_BLACK = '\033[40;1m'
    BACKGROUND_BRIGHT_RED = '\033[41;1m'
    BACKGROUND_BRIGHT_GREEN = '\033[42;1m'
    BACKGROUND_BRIGHT_YELLOW = '\033[43;1m'
    BACKGROUND_BRIGHT_BLUE = '\033[44;1m'
    BACKGROUND_BRIGHT_MAGENTA = '\033[45;1m'
    BACKGROUND_BRIGHT_CYAN = '\033[46;1m'
    BACKGROUND_BRIGHT_WHITE = '\033[47;1m'


def move(old_value):
    return old_value + random.choice([1, 2, 3, 4, 5, 6])


black_hole_text = [
    "sad",
    "oh no",
    "too bad",
    "better luck next time",
    "You have been sucked back",
    "dang",
    "boohoo",
    "bummer"
]
portals_text = [
    "woww",
    "yaayyy"
    "nailed it",
    "woohoo",
    "oh my God...",
    "up and away",
    "this never gets old"

]


def draw_board(board, players) -> None:
    for y in board:
        for _ in y:
            print("------", end="")
        print("-\n|", end="")

        for piece in y:
            found = False
            for player in players:
                if str(player) == piece.strip():
                    print(f" {Colors.BACKGROUND_BRIGHT_GREEN}{piece}{Colors.RESET} |", end="")
                    found = True
                    break
                
                
            if not found:
                if black_hole.get(int(piece.strip())) != None:
                    print(
                        f" {Colors.BACKGROUND_BRIGHT_RED}{piece}{Colors.RESET} |", end="")
                elif portal.get(int(piece.strip())) != None:
                    print(
                        f" {Colors.BACKGROUND_BRIGHT_BLUE}{piece}{Colors.RESET} |", end="")
                else:
                    print(f" {piece} |", end="")
        print()

    for _ in board[0]:
        print("------", end="")
    print("-")


def statement_generator(statement, deco):
    sides = deco * 4
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = deco * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def instructions():

    print("Portals and black holes is a copy of snakes and ladders but instead of ladders. \n We will be using portals and Black Holes will replace snakes.")
    print()
    print("To start the game we first have to select a mode \nSolo is for when you are playing alone and duo is for when you are playing with someone else")
    print("To roll the dice, the PLAYER has press 'enter'")
    print()
    print("BLUE IS FOR PORTALS \n USEFUL FOR SPEEDRUN SENDS YOU TO HIGHER LEVELS")
    print()
    print("RED IS FOR BLACK HOLES \n DANGEROUS CAN RUIN YOUR RUN")
    print()
    print("GREEN IS FOR PLAYER AND THAT'S YOU")


def welcome():
    print()
    print()
    statement_generator("WELCOME TO PORTALS", "*")
    instructions()
    print()


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "n":
            response == "yes"
            return response

        elif response == "no" or response == "n":
            response == "no"
            return response

        else:
            print("Please enter yes or no")


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input(
            "Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input(
            "Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" +
          player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def modes(question, answer, error):
    valid = False
    while not valid:
        response = input(question).strip().lower()
        for item in answer:
            if response == item[0] or response == item:
                answer = item
                return answer
        # output error if item not in list
        print(error)
        print()
def snake(player_pos):
        if black_hole.get(player_pos) != None:
            player_pos = black_hole[player_pos]
            print()
            statement_generator(random.choice(black_hole_text), "~")
            print(player_names[player_turn] + "down to " + str(player_pos))
        return player_pos

def portals(player_pos):
    if portal.get(player_pos) != None:
        player_pos = portal[player_pos]
        print()
        statement_generator(random.choice(portals_text), "#")
        print(player_names[player_turn] + "moved up to " + str(player_pos))
    return player_pos


welcome()
mode = ["solo", "duo","multi", "xxx"]


hello = modes("What mode would you like to play \nAvailable options:  Solo, Duo and Multi \n : ",
              mode, "Please enter the available modes")

player_turn = 0
if hello == "solo":
    player_names = [input("Please enter a valid name for player: ").strip()]
    print("Player name will be " + str(player_names))
    players = [0]

elif hello == "duo":
    player_names = [
        input("Please enter a valid name for player 1: ").strip(),
        input("Please enter a valid name for player 2: ").strip()
    ]
    players = [0, 0]

elif hello == "multi":
    no_players = int(input("How many players : "))
    player_names = []
    players = []
    for i in range(no_players):
        player_names.append(input("Please enter a valid name for player: "))
        players.append(0)
        
elif hello == "xxx":
    quit()
    

quesion1 = input("Lets begin \n Enter to row or xxx to quit: ")
print()
print(player_names)
life = 10
while quesion1 == "":
    players[player_turn] = move(players[player_turn])
    

    if hello == "solo":
        if players[player_turn] == snake(players[player_turn]):
            life =  life - 1
            print("you have " + str(life) + " lives out of 10 lives")
        if life <= 0:
            print("You have out of lives")
            break

    if players[player_turn] > 100:
        players[player_turn] = 100

    players[player_turn] = snake(players[player_turn])

    players[player_turn] = portals(players[player_turn])

    time.sleep(SLEEP_BETWEEN_ACTIONS)
    draw_board(board, players)

    print(player_names[player_turn] + " has moved to " + str(players[player_turn]))

    if players[player_turn] == 100:
        print()
        statement_generator(player_names[player_turn] + " has won!", "*")
        break

    quesion1 = input(statement_generator(
        "Would u like to roll again: ", "!"))
    print()
    if quesion1 == "xxx":
        print("You have quit")
        break

    player_turn = (player_turn + 1) % len(players)

