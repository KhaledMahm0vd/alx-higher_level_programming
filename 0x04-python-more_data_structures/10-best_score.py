#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key_list = list(a_dictionary.keys())
        score = 0
        best_achiever = ""
        for i in key_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                best_achiever = i
        return best_achiever
