
def statement_generator(statement, deco):
    sides = deco * 4
    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = deco * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

def instructions():
    print("you are stupid")
    print()
    print("you are op")
    print()
    print("nicely done mate")
def welcome():
    statement_generator("welcome to portals","*")
    instructions()
    print ()
    


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or  response == "n":
            response == "yes"
            return response

        elif response == "no" or response == "n":
            response == "no"
            return response

        else:
            print("Please enter yes or no")

def players():
    player1 = None
    while not player1:
        player1 =input("What name would you like to use  ").strip()
        print()
    
    player2 = None
    while not player2:
        player2 = input("what name would you like to use  ").strip()
        print()

    print("Match with be between " + player1 + " and " + player2)
    print()
    return player1, player2





welcome()
player1, player2 = players()
print()
print()
