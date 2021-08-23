def modes(question, answer, error):
    valid = False
    while not valid:
        response = input(question).strip().lower()
        for item in answer:
            if response == item[0] or response == item:
                answer = item
                print("program continues")
                
                
        # output error if item not in list
        print(error)
        print()

mode = ["solo", "duo","multi", "xxx"]

hello = modes("What mode would you like to play \nAvailable options:  Solo, Duo and Multi \n : ",
              mode, "Please enter the available modes")
