#!/usr/bin/python3

def uniq_add(my_list=[]):
    t_sum = 0
    for val in set(my_list):
        t_sum += int(val)
    return t_sum
