"""author: Anish Amul Vaidya
Question 3

Assumptions - input in taken from user after code is run and not during command line.
in case of output -  "outsider can't be determined" -> I am assuming that the input consists of only 2 words and "stop"
eg - Paraguay
     Egypt
     stop
"""

def find_outsider(input_list):
    count_dict = {}
    odd_one = []
    for element in input_list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    for key, value in count_dict.items():
        if value == 1:
            odd_one.append(key)
    if len(odd_one) == 1:
        print ("the outsider is \"" + odd_one[0] + "\"")
    elif len(odd_one) == 0:
        print("there is no outsider")
    else:
        print("outsider can't be determined")

if __name__ == "__main__":
    input_list = []
    inp = input()
    do = True
    while do:
        if inp != "stop":
            input_list.append(inp)
            inp = input()
        else:
            do = False
    # input_list = ["Paraguay", "Egypt", "Paraguay", "Paraguay", "Paraguay"]        
    find_outsider(input_list)