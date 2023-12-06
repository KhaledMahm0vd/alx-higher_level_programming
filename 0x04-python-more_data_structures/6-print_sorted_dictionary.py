#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = []
    for key, value in a_dictionary.items():
        key_list.append(key)
    for key in sorted(key_list):
        print(key + ": " + str(a_dictionary.get(key)))
