import time
import matplotlib.pyplot as plt
import random

def random_array(range_start, range_end, number_of_elements):
    return [random.randrange(range_start, range_end) for i in range(number_of_elements)]

def time_algorithm(sorting_algorithm, input_size):
    arr = random_array(0, input_size, input_size)

    t0 = time.time()

    sorting_algorithm(arr)

    t1 = time.time()

    delta_seconds = t1 - t0

    return delta_seconds * 1000 # return time difference in milliseconds

def time_algorithm_range(algorithm, input_sizes):
    return [time_algorithm(algorithm, input_size) for input_size in input_sizes]

def time_algorithms(algorithms, input_sizes):
    results = dict()
    results["Input Sizes"] = input_sizes
    results["Algorithm Performances"] = dict()
    for algorithm_name, algorithm in algorithms.items():
        results["Algorithm Performances"][algorithm_name] = time_algorithm_range(algorithm, input_sizes)
    return results

def print_results(results):
    print("Input Size".ljust(20), end='')
    for input_size in results["Input Sizes"]:
        print(str(input_size).rjust(20), end='')
    print()

    for algorithm_name, performances in results["Algorithm Performances"].items():
        print(algorithm_name.ljust(20), end='')
        for performance in performances:
            print('{:.3f} ms'.format(performance).rjust(20), end='')
        print()

def analyse(algorithms, input_sizes):
    results = time_algorithms(algorithms, input_sizes)
    print_results(results)

def visualize(algorithms, input_sizes):
    results = time_algorithms(algorithms, input_sizes)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Time in miliseconds")
    for algorithm_name, performances in results["Algorithm Performances"].items(): 
        ax.plot(results["Input Sizes"], performances, label=algorithm_name)
    ax.legend()
    plt.show()