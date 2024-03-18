#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= len(my_list)) or (idx < 0):
        return my_list
    else:
        list_dup = my_list.copy()
        list_dup[idx] = element
        return list_dup
