"""author: Anish Amul Vaidya
Question 5"""

def calculate():
    total_grains = 0
    i = 0
    belgium_surface = 30528 * 1000 * 1000
    while i < 64:
        total_grains = total_grains + 2 ** i
        i += 1
    weight = 25 * total_grains // 1000000
    length = 5 * total_grains // 1000000
    total_volume = 5 * 5 * 5 * total_grains // 1000000000
    total_height = total_volume // belgium_surface
    print (str(total_grains) + "\n")
    print (str(weight) + " kg\n")
    print (str(length) + " km\n")
    print (str(total_height) + " m\n")
    
if __name__ == "__main__":
    calculate()
    