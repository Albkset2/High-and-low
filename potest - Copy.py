

import random
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

class TerminalColors:
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

DICE_FACE = 6
player_name = "albert"

playerch1 = ("\033[33;41m   \033[33;40m   ")

def move(old_value):
    return old_value + random.choice([1, 2, 3, 4, 5, 6])

def draw_board(board) -> None:
    for y in board:
        for _ in y:
            print("------", end="")
        print("-\n|", end="")

        for piece in y:
            if str(player_pos) == piece.strip():
                print(f" {TerminalColors.BACKGROUND_BRIGHT_GREEN}{piece}{TerminalColors.RESET} |", end="")
            elif black_hole.get(int(piece.strip())) != None:
                print(f" {TerminalColors.BACKGROUND_BRIGHT_RED}{piece}{TerminalColors.RESET} |", end="")
            elif portal.get(int(piece.strip())) != None:
                print(f" {TerminalColors.BACKGROUND_BRIGHT_BLUE}{piece}{TerminalColors.RESET} |", end="")
            else:
                print(f" {piece} |", end="")
        print()
            

    for _ in board[0]:
        print("------", end="")
    print("-")



player_pos = 0


quesion1 = input("why u likw to play again: ")

while quesion1 == "":
    player_pos = move(player_pos)

    if player_pos > 100:
        player_pos = 100
    
    if black_hole.get(player_pos) != None:
        player_pos = black_hole[player_pos]
    if portal.get(player_pos) != None:
        player_pos = black_hole[player_pos]

    draw_board([ 
        [ "100", " 99", " 98", " 97", " 96", " 95", " 94", " 93", " 92", " 91" ],
        [ " 81", " 82", " 83", " 84", " 85", " 86", " 87", " 88", " 89", " 90" ],
        [ " 80", " 79", " 78", " 77", " 76", " 75", " 74", " 73", " 72", " 71" ],
        [ " 61", " 62", " 63", " 64", " 65", " 66", " 67", " 68", " 69", " 70" ],
        [ " 60", " 59", " 58", " 57", " 56", " 55", " 54", " 53", " 52", " 51" ],
        [ " 41", " 42", " 43", " 44", " 45", " 46", " 47", " 48", " 49", " 50" ],
        [ " 40", " 39", " 38", " 37", " 36", " 35", " 34", " 33", " 32", " 31" ],
        [ " 21", " 22", " 23", " 24", " 25", " 26", " 27", " 28", " 29", " 30" ],
        [ " 20", " 19", " 18", " 17", " 16", " 15", " 14", " 13", " 12", " 11" ],
        [ "  1", "  2", "  3", "  4", "  5", "  6", "  7", "  8", "  9", " 10" ],

    ])

    if player_pos == 100:
        print("You have won!")
        break

    quesion1 = input("would u like to play again: ")
    if quesion1 == "xxx":
        print("You have quit")
        break


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














