#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)+1):
        print("{:d}".format(i))
        i = i-1
    return 0