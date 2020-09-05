#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:54:33 2020

@author: vanish
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:46:58 2020

@author: vanish
"""

my_str = ""
b_arr = bytearray(my_str, "UTF-8")

answer = list()

for byte in b_arr:
    answer.append(hex(byte))    
    
final = ''
for part in answer[::-1]:
    final += part[2:]

print (answer)
print (final)