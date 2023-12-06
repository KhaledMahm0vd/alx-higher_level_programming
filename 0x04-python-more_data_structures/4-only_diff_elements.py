#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_list = list(set_1) + list(set_2)
    shared_list = list(set_1 & set_2)
    for i in common_list:
        if i in shared_list:
            common_list.remove(i)
    return set(common_list)
