
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
    print("you are gay")
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



welcome()
print()
print()
