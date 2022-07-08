import tsp
import numpy as np

def test_assert_length():
    list_of_cities = tsp.get_list_of_cities('berlin52.txt')
    cities = list_of_cities[:24]
    dist = tsp.get_distance_table(cities)
    length_of_optimal_path, optimal_path = tsp.tsp(dist)

    assert 5401.10094977983 == length_of_optimal_path

def test_assert_path():
    list_of_cities = tsp.get_list_of_cities('berlin52.txt')
    cities = list_of_cities[:24]
    dist = tsp.get_distance_table(cities) 
    length_of_optimal_path, optimal_path = tsp.tsp(dist)

    np.testing.assert_array_equal([0, 22, 19, 15, 13, 12, 10, 11, 3, 5, 23, 4, 14, 9, 8, 7, 18, 2, 16, 6, 1, 20, 17, 21], optimal_path)

def test_assert_distance():
    city1 = tsp.City(id=0, x=565.0, y=575.0)
    city2 = tsp.City(id=1, x=25.0, y=185.0)
    dist = tsp.calculate_distance(city1, city2)
    assert dist == 666.1080993352356

def test_assert_distance_table():
    list_of_cities = tsp.get_list_of_cities('berlin52.txt')
    cities = list_of_cities[:3]
    dist = tsp.get_distance_table(cities)
    np.testing.assert_array_equal([[0.0, 666.1080993352356, 281.1138559374119], [666.1080993352356, 0.0, 649.3265742290239], [281.1138559374119, 649.3265742290239, 0.0]], dist)