

def space(question, error_item, error):
    valid = False
    
    while not valid:
        response = input(question).lower
        if response == error_item:
            print(error)
        return response


hello = space("love me u nugget", None, "enter a valid answer")
print(hello)

