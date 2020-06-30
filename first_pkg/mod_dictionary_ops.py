def print_dict():
    """
    :return: Prints a user generated dictionary, line by line.
    """
    my_dict = {
    }
    my_dict["name"] = input("What is your name: ")
    my_dict["age"] = input("How old are you: ")
    my_dict["color"] = (input("What is your favorite color: "))
    for key, value in my_dict.items():
        print(key, ' : ', value)
