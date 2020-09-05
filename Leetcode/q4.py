"""author: Anish Amul Vaidya
Question 4

Assumptions - input in taken from user after code is run and not during command line. If we want to use input from command line i.e 
python q4.py 32.1
we can use sys.args[1] to retrieve temperature value (in this case 32.1)
"""

import math

e = math.e

def temp_info(temperature):
    approximation = 100 / int(temperature)
    if approximation < (e - 0.1):
        print ("you have a fever")
    elif approximation > (e + 0.1):
        print ("you have hypothermia")
    else:
        print ("you have a normal body temperature")
        
if __name__ == "__main__":
    value = input("Enter temperature in celsius\n")
    temperature = float(value)
    temp_info(temperature)