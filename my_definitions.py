def greeting():
    """
    :return: "Hello!"
    """
    return("Hello!")

def message():
    """
    :return: "This program was written by Olivia Kennedy"
    """
    return("This program was written by Olivia Kennedy")

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

def print_set():
    """
    :return: Prints a user generated set, line by line.
    """
    food_1 = input("Enter the name of a food you enjoy: ")
    food_2 = input("Enter the name of another food you enjoy: ")
    food_3 = input("Enter the name of another food you enjoy: ")
    food = (food_1, food_2, food_3)
    hobby_1 = input("Enter the name of a hobby you enjoy: ")
    hobby_2 = input("Enter the name of another hobby you enjoy: ")
    hobbies = (hobby_1, hobby_2)
    my_set = (food, hobbies)
    print(*my_set, sep = "\n")






