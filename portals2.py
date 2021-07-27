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


player1, player2 = players()