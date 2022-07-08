import time

from tsp import get_list_of_cities, get_distance_table, tsp
from memory_profiler import memory_usage
import argparse
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--amount-of-cities', metavar='N', type=int, nargs=1, help='Amount of cities')
args = parser.parse_args()
def main():
    #[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23]
    list_of_cities = get_list_of_cities('berlin52.txt')

    if (args.amount_of_cities and args.amount_of_cities[0]):
        i = args.amount_of_cities[0]
        cities = list_of_cities[:i]
        bench(cities)
    else:
        df = pd.DataFrame(columns=['# of cities', 'time in seconds'])

        for i in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]:
            cities = list_of_cities[:i]
            bench_start = time.time()
            bench(cities)
            bench_end = time.time()
            benchmark_time = bench_end - bench_start
            df.loc[len(df)] = [i, benchmark_time]
            print(f"Benchmark time for {i} cities: {benchmark_time}")
        # df['amount_of_cities'] = np.log(df['amount_of_cities'])
        df['# of cities'] = df['# of cities'].astype(int)

        sns.barplot(x='# of cities', y='time in seconds', data=df, ci=None)
        plt.savefig('filename.png')


def bench(cities):
    dist = get_distance_table(cities)
    length_of_optimal_path, optimal_path = tsp(dist)
    print(f"[Cities 1 to {len(cities)}] Length of Optimal Path:", length_of_optimal_path)
    print(f"[Cities 1 to {len(cities)}] Optimal Path: ", optimal_path)


#if __name__ == '__main__':
#    main()
main()
