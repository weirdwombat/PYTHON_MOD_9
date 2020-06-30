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
