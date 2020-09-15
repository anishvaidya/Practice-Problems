# -*- coding: utf-8 -*-

alphabets = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
my_map = {}
for i,val in enumerate(alphabets):
    my_map[val] = i
def comp(s):
    list_to_return = []
    i = 0
    while i < len(s)-1:
        if s[i] =='c' and s[i+1] == 'h':
            list_to_return.append(my_map['ch'])
            i += 2
            continue
        if s[i] == 'd' and s[i+1] == 'd':
            list_to_return.append(my_map['dd'])
            i += 2
            continue
        if s[i] == 'f' and s[i+1] == 'f':
            list_to_return.append(my_map['ff'])
            i += 2
            continue
        if s[i] == 'n' and s[i+1] == 'g':
            list_to_return.append(my_map['ng'])
            i += 2
            continue
        if s[i] == 'l' and s[i+1] == 'l':
            list_to_return.append(my_map['ll'])
            i += 2
            continue
        if s[i] == 'p' and s[i+1] == 'h':
            list_to_return.append(my_map['ph'])
            i += 2
            continue
        if s[i] == 'r' and s[i+1] == 'h':
            list_to_return.append(my_map['rh'])
            i += 2
            continue
        if s[i] == 't' and s[i+1] == 'h':
            list_to_return.append(my_map['th'])
            i += 2
            continue
        list_to_return.append(my_map[s[i]])
        i += 1
    if i == len(s):
        return tuple(list_to_return)
    list_to_return.append(my_map[s[len(s)-1]])
    # print (list_to_return)
    return tuple(list_to_return)
strings = ['abcd', 'abcdd']
strings.sort(key=comp)