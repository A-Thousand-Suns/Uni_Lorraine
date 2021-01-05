import math

def check_hexacolor(color_str):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['a', 'b', 'c', 'd', 'e', 'f']
    if (color_str[0]!= '#') or len(color_str)!=7:
        return False
    for i in color_str[1:]:
        if (i not in num) and (i not in letter):
            return False
    return True


def euclidean_distance(px, py, qx, qy):
    return math.sqrt((px-qx)*(px-qx) + (py-qy)*(py-qy))