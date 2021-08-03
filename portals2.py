def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()
 
    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()
 
    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
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

   


mode = ["solo","duo","xxx"]

hello = modes("What mode would you like to play: ", mode,"Please enter the available modes")

if hello == "solo":
    player1 = input("Please enter a valid name for player: ").strip()
    print("Your player name will be "+ player1)

elif hello == "duo":
    get_player_names()

elif hello == "xxx":
    print("you have quit ")
    


