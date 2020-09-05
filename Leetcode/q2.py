"""author: Anish Amul Vaidya
Question 2

Assumptions - I have assumed that the string will be given from command line input
ex- python q2.py "Grapandmapa Epevepe's cupuckoopoo"

"""

import sys
def convert_language(input_text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ""
    p = 0
    v = 0
    for ch in input_text:
        if ch in vowels:
            if p == 1 and v != 0 :
                v -= 1
            else:
                ans += ch
                v += 1
        elif ch == "p":
            p = 1
        else:
            ans += ch
            p = 0
            v = 0
    return ans   

if __name__ == "__main__":
    print(convert_language(sys.argv[1]))
    
    
# example input - "Epevepe's cupuckoopoo"
# Grapandmapa Epevepe's cupuckoopoo apaa
