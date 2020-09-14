# -*- coding: utf-8 -*-

my_data = [("a", 10), ("b", 5), ("c", 3), ("d", 1), ("e", 100)]

basic_sorted_ans = sorted(my_data, key=lambda x: (x[1]))

my_dict = {"a": 10,
           "b": 5,
           "c": 3,
           "d": 1,
           "e": 100
    }

ans = sorted(my_data, key=(lambda x: (my_dict[x[0]])))


from functools import cmp_to_key
def custom_sort_comparator(item1, item2):
    if my_dict[item1[0]] < my_dict[item2[0]]:
        # return negative when item1 should be placed before item2
        return -1
    else:
        # return positive when item2 should be placed before item1
        return 1

# cmp_to_key required 2 params
ans_with_method = sorted(my_data, key=cmp_to_key(custom_sort_comparator))


my_data_copy = [("a", 10), ("b", 5), ("c", 3), ("d", 1), ("e", 100)]
def custom_single_param(item):
    return my_dict[item[0]]

# just specifying key required 1 param only
ans_with_single_param = sorted(my_data, key = lambda x: (custom_single_param(x)))


my_data_copy.sort(key = cmp_to_key(custom_sort_comparator))
# in .sort the key function takes only 1 parameter and compaers on basis of what it returns
# .sort -> in place sorting
my_data_copy.sort(key=custom_single_param)

