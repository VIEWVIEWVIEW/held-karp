from math import fabs, sqrt
from typing import TypedDict
import logging as log
from itertools import combinations

# log.basicConfig(level=log.DEBUG)


class City(TypedDict):
    """City object with ID and coordinates"""
    id: int
    x: float
    y: float


def get_list_of_cities(file):
    """
    Return array of cities from file
    :param file: in the following format:
    ----
    1 565.0 575.0
    2 25.0 185.0
    3 345.0 750.0
    4 945.0 685.0
    ---
    :return: []: City
    """
    list_of_cities = []
    with open(file) as f:
        for line in f:
            try:
                _id, x, y = line.split()
                city = City(id=int(_id) - 1, x=float(x), y=float(y))  # -1 because of indexing
                if _id and x and y:
                    list_of_cities.append(city)
            except ValueError:
                # log.debug("Does not match format: %s", line)
                pass
    return list_of_cities


def calculate_distance(city_1, city_2):
    """
    Calculate distance between two cities
    :param city_1:
    :param city_2:
    :return: float
    """
    x = fabs(city_1['x'] - city_2['x'])
    y = fabs(city_1['y'] - city_2['y'])
    return sqrt(x ** 2 + y ** 2)


def get_distance_table(coords):
    """
    :param coords: Array of cities
    :return: [][]: float
    """
    dists: [[float]] = []
    n = len(coords)
    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            tmp.append(calculate_distance(coords[i], coords[j]))
        dists.append(tmp)
    return dists


def tsp(dist):
    """
    :param dist: distance matrix
    :return tuple (length, [path])
    """
    # dist: [[0.0, 666.1080993352356, 281.1138559374119],
    # [666.1080993352356, 0.0, 649.3265742290239],
    # [281.1138559374119, 649.3265742290239, 0.0]]
    n = len(dist)  # n: 3
    dp = {}

    # Path costs
    # See for bitmask magic: https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
    # The link is very impressive and imo a great explanation of how to encode state in bitmasks and store
    # data efficiently
    # Also, see the following sources:
    # https://leetcode.com/problems/find-the-shortest-superstring/discuss/194932/Travelling-Salesman-Problem


    for k in range(1, n):
        dp[(1 << k, k)] = (dist[0][k], 0)
    # dp: {(2, 1): (666.1080993352356, 0), (4, 2): (281.1138559374119, 0)}

    # Don't touch *ANYTHING* below this line

    # Iterate subsets of increasing length and cache intermediate results
    for subset_size in range(2, n):
        # itertools for power set
        for subset in combinations(range(1, n), subset_size):  # subset: (1, 2)
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:  # for each subset e.g. (1, 2), we do bitwise OR operation
                bits |= 1 << bit

            # Find the lowest distance to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)  # prev = 100; bits = 110; k = 2 (010)

                result = []
                for m in subset:
                    if m == 0 or m == k:  # ignore initial state
                        continue
                    result.append((dp[(prev, m)][0] + dist[m][k], m))
                    # [(930.4404301664358, 2)]

                dp[(bits, k)] = min(result)

    # Get all bits except the one on the far right (which is our start city)
    # 000011111 - 1 -> 000011110
    # ^^^^^^^^
    bits = (2 ** n - 1) - 1

    # get overall cost of path from initial state to final state
    result = []
    for k in range(1, n):
        result.append((dp[(bits, k)][0] + dist[k][0], k))
    optimal_path_length, parent = min(result)

    # Backtrack to get the full optimal path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        throwaway, parent = dp[(bits, parent)]
        bits = new_bits

    # Add start city (append since we are backtracking, and city #0 is the start city)
    # Ok nvm, we dont need this because all online calculators ignore it.
    # path.append(0)

    optimal_path = path[::-1]  # reverse path list

    return optimal_path_length, optimal_path


def main():
    list_of_cities = get_list_of_cities('berlin52-cut.txt')
    dist = get_distance_table(list_of_cities)

    length_of_optimal_path, optimal_path = tsp(dist)
    print("Length of optimal path", length_of_optimal_path)
    print("Optimal path:", optimal_path)


if __name__ == '__main__':
    main()
