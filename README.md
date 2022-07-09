# Quick Overview
- Find the main entrypoint here: https://github.com/VIEWVIEWVIEW/held-karp/blob/main/tsp.py#L144
- First you need to read a file with coordinates, you can find a brief description below. You can use ``get_cities()`` for that, like so:
```python3
list_of_cities = get_list_of_cities('your-file.txt')
```
- Afterwards you need to generate a 2d distance matrix. You can use ``get_distance_table()`` for that, like so:
```python3
dist = get_distance_table(list_of_cities)
```
- Finally, just pass the distance matrix to the tsp algorithm, which returns a tuple with the optimal path length as an integer, and the optimal path itself as a list:
```python3
length_of_optimal_path, optimal_path = tsp(dist)
```

# list_of_cities
In case you want to write your own data importer, make sure you return it in the following fashion:
```python3
class City(TypedDict):
    """City object with ID and coordinates"""
    id: int
    x: float
    y: float


def custom_list_of_cities_importer():
    """
    :return: []: City
    """
    list_of_cities = []
    
    for i in range(10):
      city = City(id=i, x=i * 2, y=i / 2)
      list_of_cities.append(city)

    return list_of_cities
```


## Sources
 - [Berlin52 Dataset](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/berlin52.tsp)


## How to use with other data sets
Use the following *space seperated* data format:
``numeric-id x y``

```
1 512 512
2 1337 1337
3 456 456
4 789 789
5 987 654
6 123 321
7 876 543
```

Any lines which do not follow this format are ignored.



