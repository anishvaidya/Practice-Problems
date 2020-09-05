"""author: Anish Amul Vaidya
Question 1
"""

def mapperA(directions):
    outputA = ""
    for each in directions:
        if each == "N":
            outputA += "E"
        elif each == "S":
            outputA += "W"
        elif each == "E":
            outputA += "N"
        else:
            outputA += "S"
    return outputA

def mapperB(directions):
    outputB = ""
    for each in directions:
        if each == "N":
            outputB += "W"
        elif each == "S":
            outputB += "E"
        elif each == "E":
            outputB += "S"
        else:
            outputB += "N"
    return outputB

def mapperC(directions):
    outputC = ""
    for each in directions:
        if each == "N":
            outputC += "S"
        elif each == "S":
            outputC += "N"
        elif each == "E":
            outputC += "W"
        else:
            outputC += "E"
    return outputC
    

def calculate(k):
    global mem
    if mem[k] != 0:
        return mem[k]
    if k == 1:
        mem[k] = "EENNWSWN"
        return mem[k]
    else:    
        pa_dk = mapperA(calculate(k - 1))
        dk_n = calculate(k-1) + "N"
        pc_dk = mapperC(calculate(k - 1))
        pb_dk = mapperB(calculate(k - 1))
        mem[k] = (pa_dk + "E" + pa_dk + "E" + dk_n + dk_n + calculate(k - 1) + "W" + pc_dk + "S" + pb_dk + "W" + pb_dk + "N" + calculate(k - 1))
  
    return mem[k]
    
def sleepwalker(k, start_x, start_y, hole_x, hole_y):
    global mem
    seq = path(k)
    count = 0
    x = 1
    y = 1
    inc = False
    for char in seq:
        if x == start_x and y == start_y:
            inc = True
        if x == hole_x and y == hole_y:
            return count
        if inc:
            count+=1
        if char == 'N':
            y+=1
        elif char == 'S':
            y-=1
        elif char == 'E':
            x+=1
        else:
            x-=1
    return count

def permutation(directions, way):
    if way == 'a':
        return mapperA(directions)
    elif way == 'b':
        return mapperB(directions)
    else:
        return mapperC(directions)

def path(k):
    global mem
    mem = []
    for i in range(k+1):
        mem.append(0)
    return calculate(k)
    

if __name__ == "__main__" :
   print(permutation('SEN', 'a'))
   print(permutation('SEN', 'b'))
   print(permutation('SEN', 'c'))
   print (path(1))
   print (path(2))
   print(sleepwalker(2, 3, 2, 7, 2))
   print(sleepwalker(2, 9, 6, 3, 7))
   print(sleepwalker(3, 1, 1, 1, 27))
   
   