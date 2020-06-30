"""
Program : packages_assignment.py
Author : Olivia Kennedy
Date Last Modified : 06/30/2020
This file imports modules from the package, first_pkg, and carries out the functions.
"""
import first_pkg.mod_dictionary_ops, first_pkg.mod_greeting, first_pkg.mod_set_ops

if __name__ == '__main__':
    print(first_pkg.mod_greeting.greeting())
    print(first_pkg.mod_greeting.message())
    first_pkg.mod_dictionary_ops.print_dict()
    first_pkg.mod_set_ops.print_set()
