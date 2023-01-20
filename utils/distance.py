import math


def eucludian_distance(v1, v2):
    square_distance = 0
    for i in range(len(v1)):
        square_distance += (v1[i] - v2[i]) ** 2

    return math.sqrt(square_distance)
