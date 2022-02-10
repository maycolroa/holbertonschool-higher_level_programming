#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    for key, val in new_dic.items():
        new_dic[key] = val * 2
    return new_dic
