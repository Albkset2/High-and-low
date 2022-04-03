
import random


# functions
def question_check(question, answer_list, error_message):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in answer_list:
            if response == item[0] or response == item:
                answer = item
                return answer

        # output error if item not in list
        print(error_message)
        print()


def number_checker(question, mini, maxi, error_message):

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low/ too high give
            if mini < response <= maxi:
                return response

            else:
                print(error_message)
        except ValueError:
            print(error_message)


def instruction():
    print("instruction")


def deal(pick_amount, who_deck):
    for i in range(pick_amount):
        who_deck.append(deck.pop())
yes_no = ["yes", "no"]
available_moves = ["hit", "stay", "double up"]
unavailable_moves = []
cards_amount = ["2", "3", "4", "5"]
bank_allow = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
user_deck = []
deal_deck = []
# main
play = question_check("do you want to play BlackJack", yes_no, "please answer 'yes' or 'no'")
# want to play
if play == "yes":
    # instructions
    instruct = question_check("do you want the instructions", yes_no, "please answer 'yes' or 'no'")
    if instruct == "yes":
        print(instruction)
        print()
    else:
        print()

    deck_amount = question_check("how many decks do you want to play", cards_amount, "please pick a number from 2-5")


# ######################################where the loop starts?##################################
    go = "yes"
    while go == "yes":

        bank = number_checker("how much would you like to put into the bank from 1-10", 1, 10, "please pick a number between 1 and 10")
        print("you have ${:.2f} in the bank".format(bank))

        bet = number_checker("how much would you like to bet for this round", 1, bank, "please pick a number between 1 and the amount in the bank")
        print("you bet ${:.2f} for this round".format(bet))
        # shuffle deck
        deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q"](int(deck_amount))
        random.shuffle(deck)
        # deal 2 cards
        deal(2, user_deck)
        deal(2, deal_deck)
        # show total of user
        print(user_deck)
        print("your total is {}".format())



# don't want to play
else:
    print("you quit")
    quit()